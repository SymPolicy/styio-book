# Function

{% tabs %}
{% tab title="Definition" %}
```
f(x, y) := {
    ...
}
```
{% endtab %}
{% endtabs %}

### Closure (Anonymous Function)

{% tabs %}
{% tab title="Usage" %}
```
#(x, y) => { 
    ==(x + y)==
}

#(x, y) => | x + y |
```
{% endtab %}

{% tab title="Definition" %}
```
/*
 * Bring variables into the expression.
 */

@(x, y) -> {
    x + y
}

@(x, y) -> | x + y |
```
{% endtab %}
{% endtabs %}
