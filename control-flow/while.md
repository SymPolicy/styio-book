# while

## Loop Forever

```
[...] +> {
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

```
[...] +> {
    ...
    
    ! -> _;
}
```

### + Break (With Condition)

```
// macro start: check `expr` and then reset this code block

! -> ?() -> _ 
```

{% tabs %}
{% tab title="Usage" %}
<pre><code><strong>[...] +> {
</strong>    ...
    
    !?(`expr`) -> _;
}
</code></pre>
{% endtab %}

{% tab title="Definition" %}
```
[...] -> {
    ...
    
    ! -> ?(`expr`) -> _;
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="Java" %}
<pre class="language-java"><code class="lang-java"><strong>while (true) {
</strong>    // code block
    
    if (`expr`) {
        break;
    }
}
</code></pre>
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

### + Continue

```
// macro start: do nothing

! -> {} 
```

{% tabs %}
{% tab title="Usage" %}
```
[...] +> {
    ...
    
    ! -> { };
}
```
{% endtab %}

{% tab title="Definition" %}
```
[...] -> {
    ...
    
    ! -> {};
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
        continue;
    }
}
```
{% endtab %}

{% tab title="Python" %}
```python
while True:
    ...
    
    if `expr`:
        continue
```
{% endtab %}
{% endtabs %}

## While Loop

### + Condition

```
[...] ?(`expr`) +> {
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
[0..i] +> {
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

