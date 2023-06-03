# 格式化字符串

Styio 中的 格式化字符串 (Format String) 和 字符串插值 (String Interpolation) 是 完全相同的方法.&#x20;

代码:

```
name := "Styio";

$"Hello, {name}!"
```

输出:

```
Hello, Styio!
```

### Reason

使用`${}`作为字符串插值符号的语言, 包括 Shell, JavaScript, Kotlin, Scala.&#x20;

而 C# 支持 使用 `$` 标注整个字符串, 然后在字符串内部使用 `{ }` 完成字符串插值. 不需要对于每个变量单独标注, 比较优雅, 因此 Styio 采用 C# 的字符串插值语法.&#x20;

Shell 的 `${name}` 和 `$name` 是相同的含义, 但用在字符串插值中会降低可读性, 也会带来解析上的困难. 因此采用 C# 和 Python 的方案, 使用 `{}` 标注变量.&#x20;

对于原生 `{` 和 `}` 字符的需求, 可以使用 `{{` 和 `}}` 进行转义替代. 当然, `\{` 和 `\}` 也是被允许的.&#x20;

{% tabs %}
{% tab title="C#" %}
```csharp
string name = "C#";
string text = $"Hello, {name}!";
```
{% endtab %}

{% tab title="Shell" %}
```sh
name="Shell"
echo "Hello, ${name}!"
```
{% endtab %}

{% tab title="JavaScript" %}
```javascript
let name = "Javascript";
let text = `Hello, ${name}!`;
```
{% endtab %}

{% tab title="Kotlin" %}
```kotlin
val name = "Kotlin"
println("Hello, ${name}!")
```
{% endtab %}

{% tab title="Scala" %}
```scala
val name = "Scala"
println(s"Hello, $name!")
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="Python" %}
```python
name = "Python"
print(f"Hello, {name}!")
```
{% endtab %}

{% tab title="Ruby" %}
```ruby
name = "Ruby"
text = "Hello, #{name}!"
```
{% endtab %}

{% tab title="Swift" %}
```swift
let name = "Swift"
let text = "Hello, \(name)!"
```
{% endtab %}
{% endtabs %}

### Advanced

{% embed url="https://zhuanlan.zhihu.com/p/632687543" %}
