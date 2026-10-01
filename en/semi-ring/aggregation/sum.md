> **Historical design note, not current usage guidance.** This page preserves early proposals and rationale; code may be retired or never implemented. Start at the [current guide](../../README.md) and do not infer active syntax or APIs from this page.

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
