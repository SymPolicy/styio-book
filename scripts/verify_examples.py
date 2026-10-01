#!/usr/bin/env python3
"""Verify cookbook provenance, then optionally execute pinned compiler fixtures.

No network, compiler installation, upstream checkout mutation, or shared-output
writes. A caller-supplied build label is evidence attribution, not a proof that
an executable was produced by the named source revision.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "cookbook/cases.json"
SNIPPET = re.compile(r"<!-- cookbook:([a-z0-9-]+) -->\s*```(?:styio|text)\n(.*?)\n```", re.S)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_path(value: str) -> Path:
    path = Path(value)
    if not value or path.is_absolute() or ".." in path.parts or "\\" in value or ":" in value:
        raise ValueError(f"unsafe relative path: {value!r}")
    return path


def load_manifest(path: Path = MANIFEST) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema_version") != 1:
        raise ValueError("unsupported cookbook schema")
    if not re.fullmatch(r"[0-9a-f]{40}", data.get("compiler_ref", "")):
        raise ValueError("compiler_ref must be a full commit SHA")
    ids = []
    for case in data["cases"]:
        ids.append(case["id"])
        for key in ("source", "stdout_source", "stdin_source", "stderr_source"):
            if key in case:
                safe_path(case[key])
                sha_key = "source_sha256" if key == "source" else key.replace("_source", "_sha256")
                if not re.fullmatch(r"[0-9a-f]{64}", case.get(sha_key, "")):
                    raise ValueError(f"{case['id']}: missing {sha_key}")
        if not 0 < case.get("timeout_seconds", 0) <= 120:
            raise ValueError(f"{case['id']}: timeout must be bounded")
        kinds = sum(bool(case.get(x)) for x in ("stdout_source", "stderr_source", "artifact"))
        if kinds != 1 or bool(case.get("stderr_source")) != bool(case.get("expect_failure")):
            raise ValueError(f"{case['id']}: choose one positive/negative/artifact contract")
        for asset in case.get("assets", []):
            safe_path(asset["path"])
        if "artifact" in case:
            safe_path(case["artifact"]["path"])
        for replacement in case.get("source_replacements", []):
            safe_path(replacement["new"])
            if replacement.get("count") != 1 or not replacement.get("old"):
                raise ValueError("source adaptations must name one exact path occurrence")
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate case id")
    return data


def read_source(repo: Path, ref: str, path: str, expected_hash: str) -> bytes:
    safe_path(path)
    result = subprocess.run(["git", "-C", str(repo), "show", f"{ref}:{path}"],
                            capture_output=True, timeout=30, check=True)
    if digest(result.stdout) != expected_hash:
        raise ValueError(f"pinned source hash mismatch: {path}")
    return result.stdout


def collect_case(repo: Path, ref: str, case: dict) -> dict[str, bytes]:
    files = {}
    for key in ("source", "stdout_source", "stdin_source", "stderr_source"):
        if key in case:
            sha = "source_sha256" if key == "source" else key.replace("_source", "_sha256")
            files[key] = read_source(repo, ref, case[key], case[sha])
    for asset in case.get("assets", []):
        files[asset["path"]] = read_source(repo, ref, asset["path"], asset["sha256"])
    return files


def check_snippets(all_files: dict[str, dict[str, bytes]]) -> int:
    count = 0
    normal = lambda s: re.sub(r"\s+", " ", s).strip()
    for lang in ("cn", "en"):
        for path in (ROOT / lang).rglob("*.md"):
            if any(part in {".artifacts", "_book", ".git"} for part in path.parts):
                continue
            for case_id, snippet in SNIPPET.findall(path.read_text(encoding="utf-8")):
                if case_id not in all_files:
                    raise ValueError(f"unknown code case in {path}: {case_id}")
                source = all_files[case_id]["source"].decode("utf-8")
                if not snippet.strip() or normal(snippet) not in normal(source):
                    raise ValueError(f"quoted source drift: {path.relative_to(ROOT)} / {case_id}")
                count += 1
    if count == 0:
        raise ValueError("no pinned code snippets found")
    return count


def judge(case: dict, data: dict[str, bytes], process: subprocess.CompletedProcess,
          cwd: Path) -> list[str]:
    errors = []
    if case.get("expect_failure"):
        if process.returncode <= 0:
            errors.append("expected diagnostic rejection; success or signal termination is not rejection")
        fragments = data["stderr_source"].decode("utf-8").splitlines()
        stderr = process.stderr.decode("utf-8", errors="replace")
        if not fragments or any(fragment and fragment not in stderr for fragment in fragments):
            errors.append("expected diagnostic fragment missing")
        if process.stdout:
            errors.append("negative case unexpectedly produced stdout")
    else:
        if process.returncode != 0:
            errors.append(f"compiler exited {process.returncode}")
        if "stdout_source" in data and process.stdout != data["stdout_source"]:
            errors.append("stdout differs from pinned golden")
        if "artifact" in case:
            artifact = case["artifact"]
            path = cwd / safe_path(artifact["path"])
            if not path.is_file() or path.read_bytes() != artifact["text"].encode("utf-8"):
                errors.append("artifact differs from pinned expected bytes")
    return errors


def run_case(binary: Path, case: dict, data: dict[str, bytes]) -> dict:
    with tempfile.TemporaryDirectory(prefix="styio-cookbook-") as tmp:
        cwd = Path(tmp)
        source = data["source"].decode("utf-8")
        for replacement in case.get("source_replacements", []):
            if source.count(replacement["old"]) != replacement["count"]:
                raise ValueError(f"{case['id']}: source path adaptation no longer matches")
            source = source.replace(replacement["old"], replacement["new"])
        program = cwd / "case.styio"
        program.write_text(source, encoding="utf-8")
        for asset in case.get("assets", []):
            target = cwd / safe_path(asset["path"])
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data[asset["path"]])
        try:
            result = subprocess.run([str(binary), "--file", str(program)], cwd=cwd,
                                    input=data.get("stdin_source", b""), capture_output=True,
                                    timeout=case["timeout_seconds"])
        except subprocess.TimeoutExpired:
            return {"id": case["id"], "status": "failed", "errors": ["timeout"]}
        errors = judge(case, data, result, cwd)
        record = {"id": case["id"], "status": "failed" if errors else "passed",
                  "exit_code": result.returncode, "errors": errors}
        if errors:
            record.update(stdout=result.stdout.decode("utf-8", errors="replace")[:3000],
                          stderr=result.stderr.decode("utf-8", errors="replace")[:3000])
        return record


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check-only", action="store_true")
    mode.add_argument("--run", action="store_true")
    parser.add_argument("--styio-bin", type=Path)
    parser.add_argument("--build-label")
    parser.add_argument("--case", action="append", default=[])
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    if args.run and (not args.styio_bin or not args.build_label):
        parser.error("--run requires --styio-bin and an explicit --build-label")
    try:
        manifest = load_manifest()
        files = {c["id"]: collect_case(args.source, manifest["compiler_ref"], c)
                 for c in manifest["cases"]}
        snippets = check_snippets(files)
        unknown = set(args.case) - set(files)
        if unknown:
            raise ValueError(f"unknown cases: {sorted(unknown)}")
        selected = [c for c in manifest["cases"] if not args.case or c["id"] in args.case]
        report = {"source_repository": manifest["source_repository"],
                  "compiler_ref": manifest["compiler_ref"], "static_status": "passed",
                  "checked_snippets": snippets, "mode": "run" if args.run else "check-only"}
        if args.run:
            binary = args.styio_bin.resolve(strict=True)
            report.update(binary_sha256=digest(binary.read_bytes()), build_label=args.build_label)
            report["cases"] = [run_case(binary, c, files[c["id"]]) for c in selected]
        else:
            report["cases"] = [{"id": c["id"], "status": "not_run"} for c in selected]
        encoded = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
        if args.report:
            args.report.parent.mkdir(parents=True, exist_ok=True)
            args.report.write_text(encoded, encoding="utf-8")
        print(encoded, end="")
        return int(any(c["status"] == "failed" for c in report["cases"]))
    except (OSError, ValueError, subprocess.SubprocessError) as exc:
        print(f"cookbook verification failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
