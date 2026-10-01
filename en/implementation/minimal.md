> **Historical design note, not current usage guidance.** This page preserves early proposals and rationale; code may be retired or never implemented. Start at the [current guide](../README.md) and do not infer active syntax or APIs from this page.

# Minimal

#### Do Nothing

```
...
```

#### Variable Definition (Single)

```
"@" "(" <ID> ")" ";"
```

#### Variable Assignment (Single)

\=> Mutable (Free Variable)

```
<ID> "=" <EXPR> ";"
```

\=> Immutable (Fixed Variable)

```
<ID> ":=" <EXPR> ";"
```

#### Unary Operation

```
UN_EXPR := "!" <EXPR>
```

#### Binary Operation

```
BIN_EXPR := <EXPR> "+" <EXPR>
          | <EXPR> "-" <EXPR>
          | <EXPR> "*" <EXPR>
          | <EXPR> "/" <EXPR>
```

```
          | <EXPR> ">" <EXPR>
          | <EXPR> ">=" <EXPR>
          | <EXPR> "<" <EXPR>
          | <EXPR> "<=" <EXPR>
          | <EXPR> "==" <EXPR>
          | <EXPR> "!=" <EXPR>
```

```
          | <EXPR> "&&" <EXPR>
          | <EXPR> "||" <EXPR>
```

#### Loop

```
[...] >> {
    <STMT>*
    <EXPR>?
}
```

#### IF...Then

```
? (`expr`) -> {
    ...
}
```

#### IF...Else

```
? (`expr`) :) {
    ...
} :( {
    ...
}
```
