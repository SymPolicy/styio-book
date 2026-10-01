# 当前语法与第一个程序

本页适用于已验证的下游 nightly 版本 `fd3b3e2d9a90`。其他版本的语法支持可能不同；[版本与验证说明](contributing.md)。

## 第一个程序

<!-- cookbook:hello -->
```text
"Hello, World!" -> @stdout
```

保存为 `hello.styio`，使用已构建的 `styio --file hello.styio`。预期标准输出为 `Hello, World!` 加换行。源文件：[hello_world.styio](https://github.com/Unka-Malloc/styio-nightly/blob/fd3b3e2d9a900fa58bc70641a42885c991650210/example/hello_world.styio)。

## 常用形式

| 意图 | 当前写法 | 注意事项 |
| --- | --- | --- |
| 最终绑定 | `name := expr` | 不能随后重新绑定；不等于容器元素一律不可修改 |
| 可变绑定 | `name = expr` | 绑定或重新绑定普通值 |
| 类型注解 | `value: i64 := 42` | `:` 后引用已有类型；不声明泛型参数 |
| 函数 | `# identity := (value) => value` | `#` 标记可调用绑定 |
| 有限遍历 | `[0..7] >> #(i) => { ... }` | 此范围包含两端；步长形式尚未激活 |
| 标准输入 | `value <- @stdin: i64` | 类型化拉取；与逐行迭代不同 |
| 标准输出 | `expr -> @stdout` | 单值输出；不要把 `@stdout` 当成可读来源 |
| 逐项传送 | `items >> #(item) => { ... }` | `>>` 推进 iterable；不等同于任意函数复合算子 |
| 显式复制 | `copy << items` | 与资源获取 `<-` 区分 |

### 返回与条件

返回写作 `<| expr`，不使用历史的 `== ... ==>`。条件分支写作 `?(cond) => { ... } | { ... }`；连续 guard 的组合方式见 cookbook。

## 推导的边界

未注解数值字面量归一到 `i64` 或 `f64`。空 `[]` 需要元素类型上下文。final、纯、符合约束的 callable 可以推导出可复用关系；不要写 `# f[T]` 或 `f[i64](x)`。函数参数注解还可能影响检查转换，删除注解不一定保持程序行为。

本版标准库可用范围为 `std.resource`。本书用已支持的函数调用、guard 和逐项传送来组织转换，不要求额外安装 map/filter/reduce 库。

[继续：可重复验证的 Cookbook](cookbook/chaining-and-composition.md)
