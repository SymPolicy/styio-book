# Cookbook: composition and reuse

These recipes show when guard chains reduce nesting, how to organize input, transformation and output, and how to reuse inferred functions. They target downstream nightly `fd3b3e2d9a90`; see the [version and verification notes](../contributing.md).

## 1. Eight queens: nested conditions and guard chains

The [nested program](https://github.com/Unka-Malloc/styio-nightly/blob/fd3b3e2d9a900fa58bc70641a42885c991650210/example/algorithms/eight_queens.styio) and [guard-chain program](https://github.com/Unka-Malloc/styio-nightly/blob/fd3b3e2d9a900fa58bc70641a42885c991650210/tests/features/control_flow/t12_chained_guard_eight_queens.styio) implement the same search; both programs print `92` plus a newline. The following are in-function fragments, not standalone programs.

### Nested form

<!-- cookbook:queens-nested -->
```text
?(occupied(cols, col) == 0) => {
    ?(occupied(diag_down, down) == 0) => {
        ?(occupied(diag_up, up) == 0) => {
            next_cols = add_bit(cols, col)
            next_down = add_bit(diag_down, down)
            next_up = add_bit(diag_up, up)
            count += search(row + 1, next_cols, next_down, next_up)
        }
    }
}
```

### Existing guard-chain form

<!-- cookbook:queens-guards -->
```text
?(occupied(cols, col) == 0) =>
    ?(occupied(diag_down, down) == 0) =>
        ?(occupied(diag_up, up) == 0) => {
            next_cols = add_bit(cols, col)
            next_down = add_bit(diag_down, down)
            next_up = add_bit(diag_up, up)
            count += search(row + 1, next_cols, next_down, next_up)
        }
```

The search body runs only when the column and both diagonals are free. Consecutive guards remove intermediate wrapper blocks while keeping the check order and named values. Use this when no intermediate else branch is needed. Explicit branching is clearer when individual failures require recovery. Do not mechanically collapse arbitrary blocks.

The example still contains pow2/bit-mask boilerplate. Prefer the form that is easier to understand, modify, and debug rather than choosing only by line count.

## 2. Input → transformation → output

### Line-by-line standard input

<!-- cookbook:stdin-transform -->
```text
# double_it := (x: i64) => x * 2
@stdin >> #(line) => {
  double_it(line) -> @stdout
}
```

Three input lines `10`, `20`, `30` produce three stdout lines `20`, `40`, `60`. [Complete source](https://github.com/Unka-Malloc/styio-nightly/blob/fd3b3e2d9a900fa58bc70641a42885c991650210/tests/features/stdio_input/t05_stdin_transform.styio). The input stream advances at `>>`, the closure receives each item, and the call result flows to stdout. The `x: i64` annotation participates in checked conversion at this boundary; removing it is not a formatting-only change.

### File to file

<!-- cookbook:file-transform -->
```text
@file("tests/features/stream_processing/data/input.txt") >> #(x) => {
    result = x * 2
    result -> @file("/tmp/styio_doubled.txt")
}
```

The [complete source](https://github.com/Unka-Malloc/styio-nightly/blob/fd3b3e2d9a900fa58bc70641a42885c991650210/tests/features/stream_processing/t10_full_pipeline.styio) reads the same three lines. The output bytes are `204060`, not three text lines: stdout and file output have different newline behavior. Before running, choose your own input and output paths to avoid overwriting an existing file.

Both recipes use a read-one-item → compute → write structure. Naming intermediate results often makes debugging easier than compressing everything onto one line. If your file needs one record per line, choose the separator explicitly rather than assuming stdout newline behavior.

## 3. Inference and reuse

<!-- cookbook:generic-relay -->
```text
# identity := (value) => value
# relay := (value) => identity(value)
```

The [complete fixture](https://github.com/Unka-Malloc/styio-nightly/blob/fd3b3e2d9a900fa58bc70641a42885c991650210/tests/features/inferred_generics/t05_generic_composition.styio) calls `relay(42)` and `relay("relay")`; expected stdout is `42` and `relay` on separate lines. This reuses an inferred relation of eligible final, pure callables. `identity(value)` is an ordinary call, not a new pipeline-composition operator.

The linked complete example still prints with the old alias `>_(...)`. Prefer `expr -> @stdout` in new programs.

| Rejected attempt | Diagnostic fragment at this revision | Direction for repair |
| --- | --- | --- |
| `# identity[T] ...` | `unsupported syntax in authoritative nightly parser` | Remove authored generic parameters; let the definition infer |
| `identity[i64](1)` | `indexed access requires an indexable value` | Use an ordinary call and surrounding concrete annotation when needed |
| `values := []` without element context | `empty list literal is underconstrained` | Supply a `list[T]` binding type rather than guessing a default element type |

Diagnostic wording may change between versions. For these errors, first check type context and call syntax using the repair suggestions above.

[Back to current forms](../current-language.md) · [Example sources and contribution notes](../contributing.md)
