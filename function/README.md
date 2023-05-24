# Function

{% tabs %}
{% tab title="Usage" %}
```
f(x, y) {
    ...
}
```
{% endtab %}

{% tab title="Definition" %}
```
@(x, y) >> f := {
    ...
} 
```
{% endtab %}
{% endtabs %}

### Closure (Anonymous Function)

{% tabs %}
{% tab title="Usage" %}
```
@(x, y) { 
    x + y 
}

@(x, y) | x + y |
```
{% endtab %}

{% tab title="Definition" %}
```
@(x, y) := {
    x + y
}

@(x, y) := | x + y |
```
{% endtab %}
{% endtabs %}
