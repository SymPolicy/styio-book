# BNF Form

```
VAR_DEF := "@" "(" <ID> ")"
         | "@" "(" [<ID> ["," <ID>]*]? ")"

FUNC_DEF := <ID> ":=" <DOMAIN> 
          | [<VAR_DEF>]? [">>"]? <ID> ":=" <DOMAIN>
          | [<VAR_DEF>]? [">>"]? <DOMAIN>

DOMAIN := "{" <BLOCK> "}"

BLOCK := [<STMT>]* [<EXPR>]?

STMT := <EXPR> ";"

EXPR := <ID>
      | <LITERAL>
      | <COLLECTION>
      
      | <UN_EXPR>
      | <BIN_EXPR>
      
UN_EXPR := "!" <EXPR>

BIN_EXPR := <EXPR> "+" <EXPR>
          | <EXPR> "-" <EXPR>
          | <EXPR> "*" <EXPR>
          | <EXPR> "/" <EXPR>
          | <EXPR> "^" <EXPR>
          | <EXPR> "%" <EXPR>
          
          | <EXPR> ">" <EXPR>
          | <EXPR> ">=" <EXPR>
          | <EXPR> "<" <EXPR>
          | <EXPR> "<=" <EXPR>
          | <EXPR> "==" <EXPR>
          | <EXPR> "!=" <EXPR>
          
          | <EXPR> "&&" <EXPR>
          | <EXPR> "||" <EXPR>

COLLECTION := "(" [<EXPR> ["," <EXPR>]*]? ")"
            | "[" [<EXPR> ["," <EXPR>]*]? "]"
            | "{" [<EXPR> [":" <EXPR>]*]? "}"
            | "<" [<ID> "=" <EXPR> ["," <ID> "=" <EXPR>]*]? ">"
            
LITERAL := <BOOLEAN>
         | <INTEGER>
         | <FLOAT>
         | <STRING>

EXTRA := <BOOLEAN>
       | <AGGR_OP>
       
BOOLEAN := "true"
         | "false"

AGGR_OP := "sum"
         | "count"
         | "avg"
         | "max"
         | "min"
         | "first"
         | "last"
         | "exists"

EXTERNEL_OP := "type"
             | "slice"
             | "lfind"
             | "rfind"

INFINITE := "[" <ELLIPSIS> "]"

ELLIPSIS := "..."
```
