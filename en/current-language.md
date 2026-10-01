# Current forms and your first program

This page targets verified downstream nightly revision `fd3b3e2d9a90`. Other compiler versions may support different forms; see the [version and verification notes](contributing.md).

## First program

<!-- cookbook:hello -->
```text
"Hello, World!" -> @stdout
```

Save this as `hello.styio` and run an already built compiler with `styio --file hello.styio`. Expected stdout is `Hello, World!` followed by a newline. [Complete source](https://github.com/Unka-Malloc/styio-nightly/blob/fd3b3e2d9a900fa58bc70641a42885c991650210/example/hello_world.styio).

| Intent | Current form | Boundary |
| --- | --- | --- |
| Final binding | `name := expr` | Prevents rebinding; does not imply immutable container elements |
| Mutable binding | `name = expr` | Binds or rebinds an ordinary value |
| Annotation | `value: i64 := 42` | Refers to an existing type; does not declare a generic parameter |
| Callable | `# identity := (value) => value` | `#` marks a callable binding |
| Finite iteration | `[0..7] >> #(i) => { ... }` | Both endpoints are included; step ranges are not active |
| Standard input | `value <- @stdin: i64` | Typed pull, distinct from line iteration |
| Standard output | `expr -> @stdout` | Scalar sink write; stdout is not a readable source |
| Item transfer | `items >> #(item) => { ... }` | Advances an iterable, not an arbitrary function-composition operator |
| Explicit copy | `copy << items` | Distinct from resource acquisition with `<-` |

### Return and conditionals

Write a return as `<| expr`, not the historical `== ... ==>` form. Write a conditional as `?(cond) => { ... } | { ... }`; the cookbook demonstrates consecutive guards.

## Inference boundaries

Unannotated numeric literals normalize to `i64` or `f64`. Empty `[]` needs element-type context. Eligible final, pure callables infer reusable relations; authored `# f[T]` and call-site `f[i64](x)` are rejected. A parameter annotation can also affect checked conversion, so removing it is not automatically behavior-preserving.

The standard-library surface in this version is `std.resource`. These recipes compose supported calls, guards, and item transfer without requiring an additional map/filter/reduce library.

[Continue to the reproducible cookbook](cookbook/chaining-and-composition.md)
