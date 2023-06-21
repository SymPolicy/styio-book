# Binary Operation

## BinOp.Op

<table><thead><tr><th width="141">Operator</th><th></th></tr></thead><tbody><tr><td><code>+</code></td><td>Math: Add / Plus / Positive</td></tr><tr><td><code>-</code></td><td>Math: Subtract / Minus / Negative</td></tr><tr><td><code>*</code></td><td>Math: Multiply</td></tr><tr><td><code>/</code></td><td>Math: Divide</td></tr><tr><td></td><td></td></tr><tr><td><code>**</code></td><td>Math: Power</td></tr><tr><td><code>%</code></td><td>Math: Modulo</td></tr><tr><td></td><td></td></tr><tr><td><code>!</code></td><td>Logic: Not (Boolean)</td></tr><tr><td><code>&#x26;&#x26;</code></td><td>Logic: And (Boolean)</td></tr><tr><td><code>||</code></td><td>Logic: Or (Boolean)</td></tr><tr><td></td><td></td></tr><tr><td><code>&#x26;</code></td><td>Bit: And (Integer, Boolean)</td></tr><tr><td><code>|</code></td><td>Bit: Or (Integer, Boolean)</td></tr><tr><td><code>^</code></td><td>Bit: Xor (Integer, Boolean)</td></tr><tr><td><code>&#x3C;&#x3C;</code></td><td>Bit: Left Shift (Integer)</td></tr><tr><td><code>>></code></td><td>Bit: Right Shift (Integer)</td></tr></tbody></table>

## BinOp.LHS | RHS

```
<Bool> <BinOp.Op> <Bool>
<Int> <BinOp.Op> <Int>
<Float> <BinOp.Op> <Float>
<List> <BinOp.Op> <List>
<String> <BinOp.Op> <String>

<Array[Int]> <BinOp.Op> <Int>
<Array[Float]> <BinOp.Op> <Int>
<Array[Float]> <BinOp.Op> <Float>
```

