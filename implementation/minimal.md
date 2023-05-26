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
<ID> ":""=" <EXPR> ";"
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
          | <EXPR> "<" <EXPR>
          | <EXPR> "==" <EXPR>
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
