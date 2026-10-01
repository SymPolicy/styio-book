#!/usr/bin/env python3
"""Check current/historical navigation without a renderer or network access."""
import re
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
FENCES = re.compile(r"```.*?```|<pre>.*?</pre>", re.S)
LINKS = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
CURRENT = {"README.md", "SUMMARY.md", "current-language.md", "legacy-index.md",
           "cookbook/chaining-and-composition.md", "contributing.md"}
EXTRA = {"cn": {"ji-ben-fu-hao/fu-hao-jie-xi-biao.md"},
         "en": {"essential-idea/syntax-overview.md", "essential-idea/binding.md",
                "hello-world.md", "function.md"}}

def links(path):
    text = FENCES.sub("", path.read_text(encoding="utf-8"))
    text = re.sub(r"`[^`]*`", "", text)
    for raw in LINKS.findall(text):
        raw = raw.strip()
        if raw.startswith(("https://", "http://", "#", "mailto:")):
            continue
        yield raw.split("#", 1)[0]

def check():
    errors = []
    for lang in ("cn", "en"):
        book = ROOT / lang
        files = {p.resolve() for p in book.rglob("*.md") if not any(part in {".artifacts", "_book", ".git"} for part in p.parts)}
        seen = set()
        todo = [(book / "README.md").resolve(), (book / "SUMMARY.md").resolve()]
        while todo:
            page = todo.pop()
            if page in seen:
                continue
            seen.add(page)
            if page not in files:
                errors.append(f"missing entrypoint {page}")
                continue
            for target in links(page):
                path = (page.parent / target).resolve()
                if not path.is_relative_to(book.resolve()):
                    errors.append(f"cross-root local link: {page.relative_to(ROOT)} -> {target}")
                elif not path.exists():
                    errors.append(f"broken link: {page.relative_to(ROOT)} -> {target}")
                elif path in files:
                    todo.append(path)
        for path in sorted(files - seen):
            if not any(marker in path.read_text() for marker in ("历史设计资料，非当前使用说明", "Historical design note, not current usage guidance")):
                errors.append(f"unreachable current page: {path.relative_to(ROOT)}")
        for path in sorted(files):
            rel = path.relative_to(book).as_posix()
            if rel not in CURRENT | EXTRA[lang]:
                expected = "历史设计资料，非当前使用说明" if lang == "cn" else "Historical design note, not current usage guidance"
                if expected not in path.read_text():
                    errors.append(f"unmarked historical page: {path.relative_to(ROOT)}")
    return errors

if __name__ == "__main__":
    errors = check()
    print("\n".join(errors) if errors else "PASS: both book roots are linked, reachable, and history-labelled")
    raise SystemExit(bool(errors))
