> **Historical design note, not current usage guidance.** This page preserves early proposals and rationale; code may be retired or never implemented. Start at the [current guide](../README.md) and do not infer active syntax or APIs from this page.

# I/O

1. Error handling while reading a file.

```
a = @("a.json") -> $a
    ?= Err(e) => { >_ (e) }

a = @("a.json").read()
    ?= Err(e) => { >_ (e) }
    |  Ok(o)  => { o -> $a }
```
