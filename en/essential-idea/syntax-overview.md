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
#= f(x) {
  == x ==
}

#= f(x, y) {
  == y ==
}
```

#### Function Definition (Reject Overload)

```
#: f(x, y) {
  == x + y ==
}
```

### Struct

#### Struct Definition (Accept Overload) (Danger!)

```
#= Point (
  x: f64,
  y: f64,
)

#= Point (
  x: f64,
  y: f64,
  z: f64;
)
```

#### Struct Declaration (Reject Overload)

```
#: Point (
  x: f64, 
  y: f64,
)
```

#### Struct: Extra Methods

```
#: Point (
  x: f64, 
  y: f64,
) +: {
  eval() : {
    == (x, y) ==
  }
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
z = '\n'
```

## Collection

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

### List

```
[1, 2, 3, 4, 5, 6]
```

#### Get size (length) of the list

<pre><code>list = [1, 2, 3, 4, 5, 6]

|list|

<strong>&#x3C;/> 6
</strong></code></pre>

#### Push / Append / Add an element to the tail

<pre><code>list = [1, 2, 3, 4, 5, 6]

list ]+ 7

<strong>&#x3C;/> [1, 2, 3, 4, 5, 6, 7]
</strong></code></pre>

#### Pop / Delete the last element

<pre><code>list = [1, 2, 3, 4, 5, 6]

list ]-

<strong>&#x3C;/> [1, 2, 3, 4, 5]
</strong></code></pre>

#### Reversed

<pre><code>list[&#x3C;]

<strong>&#x3C;/> [6, 5, 4, 3, 2, 1]
</strong></code></pre>

#### Get an element by index

<pre><code>list = ['a', 'b', 'c']

list[0]

<strong>&#x3C;/> a
</strong></code></pre>

#### Get index of an element

<pre><code>list = ['a', 'b', 'c']

list[?= 'b']

<strong>&#x3C;/> 1
</strong></code></pre>

#### Insert an element by index

<pre><code>list = ['a', 'b', 'd']

list[+: 2 &#x3C;- 'c']

<strong>&#x3C;/> ['a', 'b', 'c', 'd']
</strong></code></pre>

#### Insert an element to the head

<pre><code>list = ['b', 'c', 'd']

list[+: 0 &#x3C;- 'a']

<strong>&#x3C;/> ['a', 'b', 'c', 'd']
</strong></code></pre>

#### Remove an element by index

<pre><code>list = ['a', 'o', 'b', 'c']

list[-: 1]

<strong>&#x3C;/> ['a', 'b', 'c']
</strong></code></pre>

#### Remove an element by value

<pre><code>list = [1, 2, 3]

list[-: ?= 2]

<strong>&#x3C;/> [1, 3]
</strong></code></pre>

#### Remove elements by many values

<pre><code>list = [1, 2, 3]

list[-: ?^ (2, 3)]

<strong>&#x3C;/> [1]
</strong></code></pre>

#### Add elements by lambda function (Danger!)

```
list = [(1, 3), (2, 4)]

list >> (x, y) +: {
    // This is a lambda function.
}
```

#### Remove elements by lambda function (Danger!)

```
list = [(1, 3), (2, 4)]

list >> (x, y) -: {
    // This is a lambda function.    
}
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

#### Infinite Loop (With Auto Cast + Match Cases)

{% code title="Match Cases (Only One)" %}
```
x = 1

[...] >> x ?= 1 => {
  >_("x is 1")
}
```
{% endcode %}

{% code title="Match Cases (Many)" %}
```
x = 0
c = 0

[...] >> x ?= {
  0 => {
    x = 1
    
    ?(c >= 10) 
    :) {
      ^^^^^^^^
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
{% endcode %}

#### Range Iterator

```
[0..10] >> {
  
}
```

#### Range Iterator (With Auto Cast)

```
[0..10] >> x => {
  >_(x)
}
```

#### Range Iterator (With Auto Cast + Match Cases)

{% code title="Match Cases (Only One)" %}
```
[0..10] >> (x) ?= 5 => {
  >_("x is 5")
}
```
{% endcode %}

{% code title="Match Cases (Branches)" %}
```
[0..10] >> (x) ?= {
  0 => { >_("x is 0") }
  1 => { >_("x is 1") }
  _ => { >_("Default") }
}
```
{% endcode %}

#### Range Iterator (With Auto Cast + Check Is In)

```
[0..10] >> (x) ?^ (2, 3, 5, 7) => {
  >_("x is prime number")
}
```

#### Range Iterator (With Auto Cast + Check Condition)

```
[0..10] >> (x) ? (x % 2 == 0) :) {
  >_("x is even number")
}
```

#### List Iterator

```
[0, 1, 2] >> {
    
}
```

#### List Iterator (With Auto Cast)

```
[0, 1, 2] >> x => {
    >_("x")
}
```

#### List Iterator (With Auto Cast + Match Cases)

{% code title="Match Cases (Only One)" %}
```
[0, 1, 2] >> (x) ?= 0 => {
  >_("x is 0")
}
```
{% endcode %}

{% code title="Match Cases (Branches)" %}
```
[0, 1, 2, 3, 4] >> x ?= {
  0 => { >_("x is 0") }
  1 => { >_("x is 1") }
  _ => { >_("Default") }
}
```
{% endcode %}

#### List Iterator (With Auto Cast + Check Is In)

```
[0, 1, 2, 3, 4, 5] >> (x) ?^ (2, 3, 5) => {
  >_("x is prime number")
}
```

#### List Iterator (With Auto Cast + Check Condition)

```
[0, 1, 2] >> (x) ? (x % 2 == 1) :) {
  >_("x is odd number")
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

