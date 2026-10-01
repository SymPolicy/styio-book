> **Historical design note, not current usage guidance.** This page preserves early proposals and rationale; code may be retired or never implemented. Start at the [current guide](README.md) and do not infer active syntax or APIs from this page.

# Operator Overloading

| Operator | Trait |
| -------- | ----- |
| -        | Neg   |
| +        | Add   |
| -        | Sub   |
| \*       | Mul   |
| /        | Div   |
| %        | Mod   |
| !        | Not   |
| &&       | And   |
| \|\|     | Or    |
| ==       | Eq    |
| !=       | Ne    |
| >=       | Ge    |
| >        | Gt    |
| <=       | Le    |
| <        | Lt    |
| >>       | Iter  |
| ->       | Rarr  |
| <-       | Larr  |

```
Point := (x, y)

Point(x, y) +: {
    x := {
        $x 
    }
    
    y := {
        $y
    }

    // Negative
    `- $?` : {
    
    }
    
    // Addition
    `$? + {other}` : {
    
    }
    
    // Reversed Addition
    `{other} + $?` : {
    
    }
    
    // Incremental Addition
    `$? += {other}` : {
        
    }
}

// Additional Function Define And Implementation
Point +: toString() := {
    
} 
```
