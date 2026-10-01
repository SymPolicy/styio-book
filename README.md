# Styio user guide

This repository contains user-facing language guidance and a version-pinned cookbook. Compiler maintenance belongs in [styio-dev-doc](https://github.com/SymPolicy/styio-dev-doc); language semantics and accepted behavior belong in the compiler's feature specifications, source, and tests.

- [简体中文](cn/README.md)
- [English](en/README.md)

The current chapters target downstream compiler commit `fd3b3e2d9a900fa58bc70641a42885c991650210`. They do not claim that the upstream release branch or a published binary contains every demonstrated feature. Old design notes remain outside the current reading path and are marked as historical. Empty placeholder pages and the obsolete external task-board stub have been removed; Git history retains them.

## Maintain and verify

```bash
python3 scripts/check_docs.py
python3 scripts/verify_examples.py --source "$STYIO_SOURCE" --check-only
python3 scripts/verify_examples.py --source "$STYIO_SOURCE" --styio-bin "$STYIO_BIN" --run --build-label "<compiler commit and any build-only patch>"
python3 -m unittest discover -s scripts -p 'test_*.py'
```

`--check-only` verifies pinned source hashes and quoted code fragments; it never claims execution passed. Runtime verification uses a temporary directory, exact stdout or artifact expectations, negative diagnostic fragments, and a timeout. The JSON report distinguishes passed, failed, and not-run cases. The caller must identify the compiler build: a source revision alone cannot prove an executable's provenance.

The `cn/` and `en/` directories are separate book roots. Render both with the existing HonKit toolchain and check the generated links, anchors, and syntax tables:

```bash
npx honkit@6.2.2 build cn "$PWD/.artifacts/cn"
npx honkit@6.2.2 build en "$PWD/.artifacts/en"
python3 scripts/check_rendered.py .artifacts
```

Inspect the HTML visually as well; structural checks do not prove layout quality. No backend publishing configuration is changed here. Public hosting and GitBook synchronization remain separate release actions.

The `Book validation` pull-request workflow runs these source, unit-test, and HTML structure checks with read-only repository access. It does not compile or execute Styio; runtime acceptance remains a separate result tied to an identified compiler binary.

## Updating the cookbook

1. Select a compiler commit and inspect its feature contract and positive/negative fixtures.
2. Update `cookbook/cases.json`, both language chapters, and source hashes together. Do not copy a second algorithm corpus into this repository.
3. Run static checks and execute the recipes against the explicitly identified compiler build.
4. Review output, failure behavior, and the English/Chinese explanation. Record an unavailable runtime as not run.
5. Publish only after the normal human review and repository contribution process. Do not promote planned standard-library modules or old syntax into current guidance.
