# Syntax Overview

### Project

#### Import Module

```
@(
  "module"
) -> {
  
}
```

### Resource

#### Resource Declaration (Global) (Can Only Be Assigned Once)

```
@(x, y)
```

#### Resource Assignment (Immutable)

```
@(x) <- "data.csv"
```

#### Resource Definition (Immutable)

```
@(x <- "data.csv")
```

### Variable

#### Variable Declaration (Global) (Mutable)

```
x: i32
```

#### Variable Definition (Global) (Mutable)

```
x: f64 = 0.3
```

#### Variable Assignment (Global) (Mutable)

```
x = 0
```

#### Variable Assignment (Global) (Immutable)

```
x := 0
```

### Function

#### Function Declaration (Accept Overload) (Danger!)

```
#: f(x) {

}

#: f(x, y) {

}
```

#### Function Definition (Reject Overload)

```
#= f(x, y) {

}
```

### Struct

#### Struct Definition (Accept Overload) (Danger!)

```
#: Point (
  x: f64,
  y: f64,
)
```

#### Struct Declaration (Reject Overload)

```
#= Point (
  x: f64, 
  y: f64,
)
```

#### Struct: Extra Methods

```
#= Point (
  x: f64, 
  y: f64,
) +: {
  
}
```

#### Struct: Operator Overload

```
#= Any () 
+: {
  `$? + {Other}`: {}
}
```

$$
x^y
$$

<table><thead><tr><th width="284">Template (Format Expression)</th><th>Description</th></tr></thead><tbody><tr><td><pre><code>`$? + {Other}`: {}
</code></pre></td><td>Binary Addition: <code>+</code> </td></tr><tr><td><pre><code>`$? - {Other}`: {}
</code></pre></td><td>Binary Subtraction: <code>-</code></td></tr><tr><td><pre><code>`$? * {Other}`: {}
</code></pre></td><td>Binary Multiplication: <code>*</code></td></tr><tr><td><pre><code>`$? / {Other}`: {}
</code></pre></td><td>Binary Division: <code>x / y</code></td></tr><tr><td><pre><code>`$? ** {Other}`: {}
</code></pre></td><td>Power: </td></tr><tr><td><pre><code>`$? % {Other}`: {}
</code></pre></td><td>Binary Subtraction: <code>-</code></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr></tbody></table>
