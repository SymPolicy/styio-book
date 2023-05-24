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
/*
 * Define a function `f` with a block.
 * Bring variables into the scope of `f`.
 */

@(x, y) -> f := {
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
