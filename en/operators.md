# Operators

## Arithmetic Operators

<table data-full-width="false"><thead><tr><th width="135">Expression</th><th width="195">Name</th><th>Precedence</th></tr></thead><tbody><tr><td><code>+ x</code></td><td>unary positve</td><td>999</td></tr><tr><td><code>- x</code></td><td>unary negative</td><td>999</td></tr><tr><td><code>x + y</code></td><td>binary addition</td><td>702</td></tr><tr><td><code>x - y</code></td><td>binary subtraction</td><td>702</td></tr><tr><td><code>x * y</code></td><td>binary multiplication</td><td>703</td></tr><tr><td><code>x × y</code></td><td>binary multiplication</td><td>703</td></tr><tr><td><code>x / y</code></td><td>binary division</td><td>703</td></tr><tr><td><code>x ÷ y</code></td><td>binary division</td><td>703</td></tr><tr><td><code>x ^ y</code></td><td>power</td><td>704</td></tr><tr><td><code>x % y</code></td><td>modulo</td><td>703</td></tr></tbody></table>

## Bitwise Operators

| Expression  | Name                | Precedence |
| ----------- | ------------------- | ---------- |
| `~ x`       | bitwise NOT         | 999        |
| `x & y`     | bitwise AND         | 303        |
| `x ⊻ y`     | bitwise XOR         | 302        |
| `x ⊼ y`     | bitwise NAND        | 302        |
| `x ⊽ y`     | bitwise NOR         | 302        |
| `x \| y`    | bitwise OR          | 301        |
|             |                     |            |
| `lhs(x, y)` | bitwise left shift  | 701        |
| `rsh(x, y)` | bitwise right shift | 701        |

Operators for bitwise XOR, NAND, NOR are derived from [Julia](https://docs.julialang.org/en/v1/manual/mathematical-operations/), they can be renamed to whatever you want in Styio. Since the opretors are not on most keyboards, it is strongly recommended to rename them as the following:

| Expression | After Renaming |
| ---------- | -------------- |
| `x ⊻ y`    | `x XOR y`      |
| `x ⊼ y`    | `x NAND y`     |
| `x ⊽ y`    | `x NOR y`      |

Traditional operators of bitwise left shift (<<) and right shift (>>) operations conflict with the iteration operator (>>) of Styio. Therefore, we use function as substitution. They are defined in the "bitwise" library, and are treated the same as other bitwise operators ( `~`, `&`, `|`, ...)

```
@<bitwise>

a = 4, b = 1
left_shift = lsh(a, b)
right_shift = rsh(a, b)
```

## Logic Operators

| Expression | Name        | Precedence |
| ---------- | ----------- | ---------- |
| `~ x`      | logical NOT | 999        |
| `x && y`   | logical AND | 203        |
| `x ⊕ y`    | logical XOR | 202        |
| `x \|\| y` | logical OR  | 201        |

