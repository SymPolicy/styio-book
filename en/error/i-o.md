# I/O

1. Error handling while reading a file.

```
a = @("a.json") -> $a
    ?= Err(e) => { >_ (e) }

a = @("a.json").read()
    ?= Err(e) => { >_ (e) }
    |  Ok(o)  => { o -> $a }
```
