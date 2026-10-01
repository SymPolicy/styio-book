# Version, example sources, and contributions

Use this appendix when updating the book or reproducing its example results. Learning Styio does not require understanding compiler modules, maintenance gates, or release workflows.

## Supported revision

The current guide and cookbook target downstream compiler commit `fd3b3e2d9a900fa58bc70641a42885c991650210`. This is a source compatibility boundary, not a claim that the upstream release or every installed `0.0.1` binary supports the same features.

The examples ran against that language source plus build candidate `85e41b90c7231b8a263b5b2c88f17fbd5833a078`. The candidate changes only CMake, maintenance routing, tests, and documentation; it does not change the C++ language implementation. Build: GCC 14, LLVM 18.1.8, Release, Tree-sitter enabled, ICU disabled. Executable SHA-256: `2b0120e9a066dfdfc9f20cade97fdac5af9953f74e3780bd61952d9874d7c3a0`.

All 6 positive and 3 negative cases met expectations, and all 12 quoted fragments in the two languages matched the pinned sources. This verifies cookbook behavior, not the compiler's entire test suite or release gates.

## Traceable sources

- [Active Syntax Map](https://github.com/Unka-Malloc/styio-nightly/blob/fd3b3e2d9a900fa58bc70641a42885c991650210/docs/design/syntax/ACTIVE-SYNTAX.md)
- [Feature specifications](https://github.com/Unka-Malloc/styio-nightly/blob/fd3b3e2d9a900fa58bc70641a42885c991650210/docs/design/syntax/features/README.md)
- [Standard-library surface](https://github.com/Unka-Malloc/styio-nightly/blob/fd3b3e2d9a900fa58bc70641a42885c991650210/library/README.md)

Complete sources, stdin, expected results, and hashes are registered in this book repository's `cookbook/cases.json`. The verifier reads files at the pinned commit rather than copying another algorithm corpus. The file-conversion case adapts only `/tmp/styio_doubled.txt` to `doubled.txt` inside an isolated temporary directory; expected output remains the exact bytes `204060`.

## Reproduce

From the book repository root, set `STYIO_SOURCE` to a compiler checkout containing the pinned commit and `STYIO_BIN` to an executable with known build provenance:

```bash
python3 scripts/check_docs.py
python3 scripts/verify_examples.py --source "$STYIO_SOURCE" --check-only
python3 scripts/verify_examples.py --source "$STYIO_SOURCE" --styio-bin "$STYIO_BIN" --run --build-label "<compiler commit and build-only patch>"
python3 -m unittest discover -s scripts -p 'test_*.py'
```

Static checking never claims execution passed. Runtime reports separately record outcomes, exit codes, and the binary fingerprint. Negative cases must produce the expected diagnostic rejection; a crash is not a pass. The build label is supplied by the caller, and a fingerprint alone does not prove provenance.

## Keep the guide current

Choose a new compiler revision, update both language explanations and the source hashes and expectations together, execute positive and negative cases, and inspect the HTML. If execution is unavailable, record it as not run rather than reusing an older revision's pass. Current guidance describes verified behavior. Design rationale and unresolved proposals belong in the [historical notes](legacy-index.md); Git preserves revision history.

The main chapters teach users to write Styio programs. Compiler internals and development procedures belong in the separate [styio-dev-doc](https://github.com/SymPolicy/styio-dev-doc).

[Back to the user guide](README.md)
