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
