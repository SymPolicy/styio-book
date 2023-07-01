# Syntax Overview

### Hello, World!

```
>_("Hello, Styio!")
```

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

### Basic Type

#### Boolean

```
x = $T

x = $F
```

#### Integer

```
x : i32 = 0
```

#### Float

```
y : f64 = 0.0
```

#### Char

```
z : '\n'
```

### Collection

#### String

```
"Hello, Styio!"
```

```
'Hello, Styio!'
```

#### Format String

```
name = "Styio"

"Hello, {name}!"
```

```
name = 'Styio'

'Hello, {name}!'
```

#### Verbatim String (Resource)

```
@"Hello, World!"
```

```
@'Hello, World!'
```

#### Raw String

```
"""
Why do you need this?
"""
```

```
'''
Why do you need this?
'''
```

#### Tuple

```
(0, 1, 2)
```

#### Array

```
x: i32[100] = [0..]
```

#### List

```
[0, 1, 2]
```

#### Record

```
< Name = "Alice", 
  Age = 15,
>
```

#### Dictionary

```
{
  "A": "Alice",
  "B": "Bob",
}
```

## Control Flow

### Condition / Cases

#### if ... then ... else ...

```
?( /* Condition */ ) :) {
    
} :( {

}
```

#### match

```
val ?= {
  0 => {
    // Do Something
  } 
  
  1 => {
    // Do Something
  }
  
  _ => {
    // Do Something
  }
}
```

### Loop / Iteration

#### Infinite Loop

```
[...] >> {

}
```

#### Infinite Loop (With Intermediate Connection Between Scopes <- ICBSLayer)

```
x = 0
c = 0

[...] >> x ?= {
  0 => {
    x = 1
    
    ?(c >= 10) 
    :) {
      ^^^^^^^^^^
    }
  }
  
  1 => {
    x = 0
    c = c + 1
  }
  
  _ => {
    !!! <- "You should not reach this line, and there must be something wrong."
  }
}
```

#### Range Iterator

```
[0..10] >> {
  
}
```

#### Range Iterator (With Intermediate Connection Between Scopes <- ICBSLayer)

```
[0..10] >> x => {
  >_(x)
}
```

```
[0..10] >> x ?= 5 => {
  >_("x is 5")
}
```

```
[0..10] >> x ?^ (6, 7) => {
  >_("x is either 6 or 7")
}
```

```
[0..10] >> x ?(x % 2 == 0) :) {
  >_("x is even")
}
```































































### Operator Overload

```
#= This () 
+: {
  `$? + {Other}`: {}
}
```

<table><thead><tr><th width="309">Template (Format Expression)</th><th>Description</th></tr></thead><tbody><tr><td><pre><code>`- $?` : {}
</code></pre></td><td>Negative: <code>- This</code></td></tr><tr><td><pre><code>`$? + {Other}` : {}
</code></pre></td><td>Binary Addition: <code>This + Other</code></td></tr><tr><td><pre><code>`$? - {Other}` : {}
</code></pre></td><td>Binary Subtraction: <code>This - Other</code></td></tr><tr><td><pre><code>`$? * {Other}` : {}
</code></pre></td><td>Binary Multiplication: <code>This * Other</code></td></tr><tr><td><pre><code>`$? / {Other}` : {}
</code></pre></td><td>Binary Division: <code>This / Other</code></td></tr><tr><td><pre><code>`$? ** {Other}` : {}
</code></pre></td><td>Math: Power {Base: <code>This</code>, Exponent: <code>Other</code>}</td></tr><tr><td><pre><code>`$? % {Other}` : {}
</code></pre></td><td>Math: Modulo {Dividend: <code>This</code>, Divisor: <code>Other</code>}</td></tr><tr><td><pre><code>`{Other} + $?` : {}
</code></pre></td><td>Reversed Addition: <code>Other + This</code></td></tr><tr><td><pre><code>`{Other} - $?` : {}
</code></pre></td><td>Reversed Addition: <code>Other - This</code></td></tr><tr><td><pre><code>`{Other} * $?` : {}
</code></pre></td><td>Reversed Addition: <code>Other * This</code></td></tr><tr><td><pre><code>`{Other} / $?` : {}
</code></pre></td><td>Reversed Addition: <code>Other / This</code></td></tr><tr><td><pre><code>`{Other} ** $?` : {}
</code></pre></td><td>Math: Power {Base: <code>Other</code>, Exponent: <code>This</code>}</td></tr><tr><td><pre><code>`{Other} % $?` : {}
</code></pre></td><td>Math: Modulo {Dividend: <code>Other</code>, Divisor: <code>This</code>}</td></tr><tr><td><pre><code>`$? += {Other}` : {}
</code></pre></td><td><code>Other += This</code></td></tr><tr><td><pre><code>`$? -= {Other}` : {}
</code></pre></td><td><code>Other -= This</code></td></tr><tr><td><pre><code>`$? *= {Other}` : {}
</code></pre></td><td><code>Other *= This</code></td></tr><tr><td><pre><code>`$? /= {Other}` : {}
</code></pre></td><td><code>Other /= This</code></td></tr><tr><td><pre><code>`$? %= {Other}` : {}
</code></pre></td><td><code>Other %= This</code></td></tr><tr><td><pre><code>`! $?` : {}
</code></pre></td><td>Logic NOT: <code>! This</code></td></tr><tr><td><pre><code>`$? &#x26;&#x26; {Other}` : {}
</code></pre></td><td>Logic AND: <code>This &#x26;&#x26; Other</code></td></tr><tr><td><pre><code>`$? || {Other}` : {}
</code></pre></td><td>Logic OR: <code>This || Other</code></td></tr><tr><td><pre><code>`$? ^ {Other}` : {}
</code></pre></td><td>Logic XOR: <code>This || Other</code></td></tr><tr><td><pre><code>`$? &#x26; {Other}` : {}
</code></pre></td><td>Bit AND: <code>This &#x26; Other</code></td></tr><tr><td><pre><code>`$? | {Other}` : {}
</code></pre></td><td>Bit OR: <code>This | Other</code></td></tr><tr><td><pre><code>`$? >> {Other}` : {}
</code></pre></td><td>Bit Right Shift: <code>This >> Other</code></td></tr><tr><td><pre><code>`$? &#x3C;&#x3C; {Other}` : {}
</code></pre></td><td>Bit Left Shift: <code>This &#x3C;&#x3C; Other</code></td></tr><tr><td><pre><code>` % |$?| ` : {}
</code></pre></td><td>Method: Get size (length) of <code>This</code></td></tr><tr><td><pre><code>` % "$?" ` : {}
</code></pre></td><td>Method: Get string of <code>This</code></td></tr><tr><td><pre><code>`% :&#x3C; $?` : {}
</code></pre></td><td>Method: Get type of <code>This</code></td></tr><tr><td><pre><code>`$?[{Item}]` : {}
</code></pre></td><td>Method: Get <code>Item</code> of <code>This</code></td></tr><tr><td><pre><code>`$?[{Item}] = {Value}` : {}
</code></pre></td><td>Method: Set <code>Item</code> of <code>This</code> as <code>Value</code></td></tr><tr><td><pre><code>`$?.{Attr}` : {}
</code></pre></td><td>Method: Get <code>Attr</code> of <code>This</code></td></tr><tr><td><pre><code>`$?.{Attr} = {Value}` : {}
</code></pre></td><td>Method: Set <code>Attr</code> of <code>This</code> as <code>Value</code></td></tr><tr><td><pre><code>`$?[&#x3C;]` : {}
</code></pre></td><td>Method: Get reversed collection.</td></tr><tr><td><pre><code>`$? ?^ {List}` : {}
</code></pre></td><td>Method: Check if <code>This</code> in <code>List</code> or not.</td></tr><tr><td><pre><code>`$? >>` : {}
</code></pre></td><td>Iterator: Implement an iterator for <code>This</code> collection.</td></tr><tr><td><pre><code>`$?()` : {}
</code></pre></td><td>Trigger: When an instance of <code>This</code> is called, do ...</td></tr><tr><td><pre><code>`$?(x, y)` : {}
</code></pre></td><td>Trigger: When an instance of <code>This</code> is called, with arguments of <code>(x, y)</code>, do ...</td></tr><tr><td><pre><code>`$?(*, **)` : {}
</code></pre></td><td>Trigger: When an instance of <code>This</code> is called, with optional arguments of <code>*</code>, and keyword arguments of <code>**</code>, do ...</td></tr></tbody></table>

