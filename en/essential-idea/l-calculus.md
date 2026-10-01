> **Historical design note, not current usage guidance.** This page preserves early proposals and rationale; code may be retired or never implemented. Start at the [current guide](../README.md) and do not infer active syntax or APIs from this page.

# λ-Calculus

```
#(f) => {
    #(x) => {
       == f(x) ==> 
    }
}
```

{% tabs %}
{% tab title="Lisp" %}
```lisp
(lambda (f) 
    (lambda (x) 
        (f x)
    )
)
```
{% endtab %}

{% tab title="Ruby" %}
```ruby
lambda { |f| 
    lambda {|x| 
        f[x]
    }
}
```
{% endtab %}
{% endtabs %}
