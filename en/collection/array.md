# Array

Array is an aggregate type in LLVM, which is arranges elements sequentially in memory.

Array in Styio can be declared as the following:

#### `Array[Size]`

```
i32[] = [0, 1, 2, 3]

i32[100] = [0..]
```

Besides, an array can also be deduced from `List` and `Tuple` types.

**Rule: If a collection is confirmed that its size would not be changed in the future, it will be converted to an array.**

A tuple of numbers with the same type will be converted to an array.
