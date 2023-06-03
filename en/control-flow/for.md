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
@(i) -> [0..10] >> {
    ...
}
```

#### Syntax Sugar

```
@i[0..10] >> {
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
