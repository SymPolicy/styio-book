# Cookbook：组合与复用

本章展示通用算法与实用程序的写法：什么时候用连续 guard 减少嵌套，怎样组织输入、转换与输出，以及怎样复用可推导的函数。示例适用于下游 nightly `fd3b3e2d9a90`；[版本与验证说明](../contributing.md)。

## 1. 八皇后：从嵌套条件到连续 guard

[完整嵌套版本](https://github.com/Unka-Malloc/styio-nightly/blob/fd3b3e2d9a900fa58bc70641a42885c991650210/example/algorithms/eight_queens.styio)与[完整连续 guard 版本](https://github.com/Unka-Malloc/styio-nightly/blob/fd3b3e2d9a900fa58bc70641a42885c991650210/tests/features/control_flow/t12_chained_guard_eight_queens.styio)实现同一个搜索；两份程序都输出 `92` 加换行。下面是函数内部片段，不能单独执行。

### 先看嵌套写法

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

### 再看仓库已有的连续 guard

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

只有列、两个对角线都未被占用时，才执行最后的搜索体。连续 guard 去掉中间包裹块，保留检查次序与最内层命名值。适用于没有中间 else 分支的筛选；需要为某次失败写恢复动作时，显式分支更清楚。不要把任意块都机械折叠。

这组例子仍有 pow2/位掩码样板。选择写法时，以是否容易理解、修改和排查错误为准，而不只看行数。

## 2. 输入 → 转换 → 输出

### 标准输入的逐行转换

<!-- cookbook:stdin-transform -->
```text
# double_it := (x: i64) => x * 2
@stdin >> #(line) => {
  double_it(line) -> @stdout
}
```

输入三行 `10`、`20`、`30`，预期 stdout 为三行 `20`、`40`、`60`。[完整源码](https://github.com/Unka-Malloc/styio-nightly/blob/fd3b3e2d9a900fa58bc70641a42885c991650210/tests/features/stdio_input/t05_stdin_transform.styio)。`@stdin >>` 推进输入流，`#(line)` 接收当前项，调用结果写入 stdout。`x: i64` 不只是装饰：在此边界涉及检查转换；不能为了缩短写法直接删除参数注解。

### 文件到文件

<!-- cookbook:file-transform -->
```text
@file("tests/features/stream_processing/data/input.txt") >> #(x) => {
    result = x * 2
    result -> @file("/tmp/styio_doubled.txt")
}
```

[完整源码](https://github.com/Unka-Malloc/styio-nightly/blob/fd3b3e2d9a900fa58bc70641a42885c991650210/tests/features/stream_processing/t10_full_pipeline.styio)读取同样的三行。文件输出字节是 `204060`，不是三行文本；标准输出与文件序列化的换行行为不同。运行前请换成自己的输入、输出路径，避免覆盖已有文件。

两例共享“读取一项 → 计算 → 写出”的结构。逐步命名中间结果，通常比压缩成一行更方便调试。需要逐行文件输出时，先明确自己的分隔方式，不要直接照搬 stdout 的换行预期。

## 3. 推导与复用

<!-- cookbook:generic-relay -->
```text
# identity := (value) => value
# relay := (value) => identity(value)
```

[完整测试](https://github.com/Unka-Malloc/styio-nightly/blob/fd3b3e2d9a900fa58bc70641a42885c991650210/tests/features/inferred_generics/t05_generic_composition.styio)分别调用 `relay(42)` 和 `relay("relay")`，预期为 `42`、`relay` 两行。此处复用的是 final、纯 callable 的推导关系，调用仍是普通 `identity(value)`。它没有定义新的管道函数组合算子。

链接中的完整示例仍使用旧输出别名 `>_(...)`；新程序推荐 `expr -> @stdout`。

### 常见失败与修正方向

| 不支持的尝试 | 当前诊断片段 | 修正方向 |
| --- | --- | --- |
| `# identity[T] ...` | `unsupported syntax in authoritative nightly parser` | 省去源代码泛型参数列表，让定义推导 |
| `identity[i64](1)` | `indexed access requires an indexable value` | 写普通调用，用周围具体注解提供必要上下文 |
| `values := []` 无元素上下文 | `empty list literal is underconstrained` | 给绑定明确 `list[T]` 类型，不猜默认元素类型 |

诊断措辞可能随版本变化。遇到这些错误，先按修正方向检查类型上下文和调用形式。

[返回当前语法](../current-language.md) · [示例来源与贡献说明](../contributing.md)
