> **Historical design note, not current usage guidance.** This page preserves early proposals and rationale; code may be retired or never implemented. Start at the [current guide](../README.md) and do not infer active syntax or APIs from this page.

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
