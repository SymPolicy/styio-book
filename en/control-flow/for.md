> **Historical design note, not current usage guidance.** This page preserves early proposals and rationale; code may be retired or never implemented. Start at the [current guide](../README.md) and do not infer active syntax or APIs from this page.

# for

#### Definition

```
@(i): int = 0;
[...] >> {
    ...
    
    i = i + 1;
    ?(a == 10) -> {
        ! -> ();
    };
}
```

#### Simplify

```
[0..10] |i| >> {
    ...
}
```

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
