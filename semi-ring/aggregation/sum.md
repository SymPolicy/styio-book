# sum

{% tabs %}
{% tab title="Definition" %}
```markup
R(k, v)... | sum(k.revenue) |
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="SDQL" %}
```
sum (<k, v> in R) if (k != None) then k.revenue else 0
```
{% endtab %}
{% endtabs %}
