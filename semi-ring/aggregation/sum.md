# sum

{% tabs %}
{% tab title="Definition" %}
<pre class="language-markup"><code class="lang-markup"><strong>@(k, v) -> R >> | (k != ~) ? sum(k.revenue) : 0 |
</strong></code></pre>
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="SDQL" %}
```
sum (<k, v> in R) if (k != None) then k.revenue else 0
```
{% endtab %}
{% endtabs %}
