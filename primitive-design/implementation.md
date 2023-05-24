# Implementation

```
// Code Block
{
    [<stmt>]*
    [<expr>]?
}

// (infinite) loop
[...] {
    
}

// record
"<" [<ID> "=" <EXPR> ["," <ID> "=" <EXPR>]*]? ">"

// dictionary
"{" [<ID> "->" <EXPR> ["," <ID> "->" <EXPR>]*]? "}"

// dictionary in python style
"{" [<ID> ":" <EXPR> ["," <ID> ":" <EXPR>]*]? "}"

// define function
f := {
    
}

// send variable to domain (function) (variable)
@(x, y) -> f := {
    
}
```
