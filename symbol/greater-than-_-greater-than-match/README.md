# ?= { => , \_ => } (Match)

## Match: \`?= { => }\`&#x20;

### Variable

```
/*
 * Check if x matches any of the cases below.
 * `_` means default case.
 */

x ?= {
    1 => { ... };
    2 => { ... };
    3 => { ... };
    _  => { ... };
}
```

### Function

<pre><code><strong>/*
</strong><strong> * `#?` represents one (and only one) argument of the function `endswith`.
</strong><strong> * `#? ' will be assigned with ".txt" ".csv" and ".json" in sequence.
</strong><strong> * Check if file_name.endswith(#?) is true for all cases below.
</strong><strong> * `_` means default case.
</strong><strong> */
</strong><strong>
</strong><strong>file_name.endswith(#?) ?= {
</strong>    ".txt" => { ... };
    ".csv" => { ... };
    ".json" => { ... };
    _  => { ... };
}
</code></pre>
