# for

#### Definition

```
[...] >> {
    ...
    
    ? (`expr`) -> {
        ! -> ();
    }
}
```

{% tabs %}
{% tab title="Syntax Sugar" %}
```
@i[0..10] >> {
    ...
}
```
{% endtab %}

{% tab title="Usage" %}
```
@(i) -> [0..10] >> {
    ...
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="Python" %}
```python
for i in range(0, 10):
    ...
```
{% endtab %}
{% endtabs %}

```
```
