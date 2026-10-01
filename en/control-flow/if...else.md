> **Historical design note, not current usage guidance.** This page preserves early proposals and rationale; code may be retired or never implemented. Start at the [current guide](../README.md) and do not infer active syntax or APIs from this page.

# if...else

#### Basic

```
// if -> then
? (`expr`) -> {
    ...
}

// else
? !(`expr`) -> {
    ...
}
```

#### Simplify

```
? (`expr`) :) {
    ...
} :( {
    ... 
}
```

{% tabs %}
{% tab title="Java" %}
```java
if (`expr`) {
    // code block
} else {
    // code block
}
```
{% endtab %}

{% tab title="Python" %}
```python
if `expr`:
    ...
else:
    ...
```
{% endtab %}
{% endtabs %}

### Ternary Operator

```
(`expr`) ? `then` : `else`
```
