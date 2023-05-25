# if...else

{% tabs %}
{% tab title="Usage" %}
```
// if
(`expr`) ? {
    // then
} : (`expr`) ? {
    // else if
} : {
    // else 
}

(`expr`) ? `then` : `else`
```
{% endtab %}

{% tab title="Definition" %}
```
? (`expr`) :) {
    ...
} :( {
    ... 
}
```
{% endtab %}
{% endtabs %}

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
