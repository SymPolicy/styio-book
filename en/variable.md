> **Historical design note, not current usage guidance.** This page preserves early proposals and rationale; code may be retired or never implemented. Start at the [current guide](README.md) and do not infer active syntax or APIs from this page.

# Variable

#### Variable Declaration

```
@(x, y)
```

\=> **+ Type**

```
@(
    x: i32,
    y: f64,
)
```

\=> **+ Optional Type**

```
@(
    x: i32 | f64 | None
)
```

#### Resource Initialization (Immutable)

_Resources can't be changed once initialized._

```
@(x <- 1, y <- 2)
```

#### Variable Declaration => Assignment

\=> Mutable

```
@(x, y) = (1, 2)
```

\=> Immutable

_Once a variable is assigned a value using the walrus symbol `:=`, it becomes **immutable**._

```
@(x, y) := (1, 2)
```

#### Adaptive Transformation

_This is equivalent to resources initialization._

```
@(x, y) <~ (1, 2)
```
