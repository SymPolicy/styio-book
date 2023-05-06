# sum

{% tabs %}
{% tab title="Usage" %}
```
R(@k, @v) +> {k: v}
```
{% endtab %}

{% tab title="Definition" %}
```
@(k, v) -> R -> !(+) -> {k: v}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="SDQL" %}
```
sum (<k, v> in R) {k -> v}
```
{% endtab %}
{% endtabs %}
