# while

## Loop Forever

```
[...] -> {
    ...
}
```

{% tabs %}
{% tab title="Java" %}
<pre class="language-java"><code class="lang-java">while (true) {
<strong>    // code block
</strong>}
</code></pre>
{% endtab %}

{% tab title="Python" %}
```python
while True:
    ...
```
{% endtab %}
{% endtabs %}

### + Break

{% tabs %}
{% tab title="First Tab" %}
```
[...] -> {
    ...
    
    !?(`expr`);
}
```
{% endtab %}

{% tab title="Definition" %}
```
[...] -> {
    ...
    
    ! <- ?();
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="Java" %}
```java
while (true) {
    // code block
    
    if (`expr`) {
        break;
    }
}
```
{% endtab %}

{% tab title="Python" %}
```python
while True:
    ...
    
    if `expr`:
        break
```
{% endtab %}
{% endtabs %}

## While Loop

### + Condition

```
[...] ?(`expr`) -> {
    ...
}
```

{% tabs %}
{% tab title="C/C++" %}
```cpp
while (`expr`) {
    // code block
}
```
{% endtab %}

{% tab title="Java" %}
```java
while (`expr`) {
    // code block
}
```
{% endtab %}

{% tab title="Python" %}
```python
while `expr`:
    ...
```
{% endtab %}
{% endtabs %}

### + Increment Element

```
[0..i] -> {
    ...
}
```

{% tabs %}
{% tab title="Java" %}
```java
int i = 0;

while (true) {
    // code block
    
    i += 1;
}
```
{% endtab %}

{% tab title="Python" %}
```python
i = 0

while True:
    ...

    i += 1
```
{% endtab %}
{% endtabs %}

