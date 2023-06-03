# Cases



```
"@" <ID>
"@" [<ID> ["," <ID>]*]?

"@" "(" <ID> ")"
"@" "(" [<ID> ["," <ID>]*]? ")"

[<ID>|<Int>|<Float>] ["+"|"-"|"*"|"**"|"/"|"%"] [<ID>|<Int>|<Float>]

"[" [[<ElemExpr>] ["," <ElemExpr>]*]? "]"

ElemExpr := <ID>
          | <Int>
          | <Float>

"[" "." ["."]* "]"
```
