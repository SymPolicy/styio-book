# 资源标识符

Styio 的设计理念是**资源调度**, 而 `@` 就是 资源标识符.&#x20;

### Variable

Styio 使用 `@` 定义变量, 以及初始化变量.

\=> 自由变量 (可变 Mutable)

```
@(x, y)
```

\=> 声明类型(Declare Type), 赋值(Assign), 可变(Mutable).&#x20;

```
@(x: int = 0)
```

\=> 固定变量 (不可变 Immutable)

```
@(x := 0)
```

\=> **可变(Mutable):** 读取文件(Read File), 解析格式(Parse -> Auto Cast), 赋值(Assign).

```
@(d <- "data.csv")
```

\=> **不可变(Immutable):** 读取文件(Read File), 解析格式(Parse -> Auto Cast), 赋值(Assign).

```
@(d := <- "data.csv")
```

{% hint style="info" %}
Variable 的定义与赋值包含 Syntax Sugar:

1. `@(x: int = 0)` 可以被降级为

```
@(x: int);
x = 0;
```

2. `@(x := 0)` 可以被降级为

```
@(x: int);
x := 0;
```

3. `@(d <- "data.csv")` 可以被降级为

```
@(d: Dict[Record]);
d <- @("data.csv")
```

4. `@(d := <- "data.csv")` 可以被降级为

```
@(d: Dict[Record]);
d <- @("data.csv");

```
{% endhint %}

## Verbatim text (Raw String) <a href="#verbatim-text----in-variables-attributes-and-string-literals" id="verbatim-text----in-variables-attributes-and-string-literals"></a>

@ 修饰的字符串被解析为 **逐字文本 (原生字符串)**, 忽略任何转义符号.

#### 示例 1

```
@"\\"
```

输出:

```
\\
```

#### 示例 2

```
"\\"
```

输出:

```
\
```

### File

文件路径 (File Path) 是 **逐字文本**.

```
@("./data.csv")
```

### URL

URL 连接(Link) 也是 **逐字文本**.

```
@("https://docs.styio.org")
```

### Package

包(Package) 以 文件路径(File Path) 或 URL 连接(Link) 的格式 导入(Import)

```
@("path/to/package")
```

包路径 (Package Path) 也是 **逐字文本**.

```
@("path\to\package")
```

{% hint style="info" %}
Verbatim Text 是 基础语法(Essential), 不可被降级拆解.
{% endhint %}
