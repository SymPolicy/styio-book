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
    x : {
        $x 
    }
    
    y : {
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
Point +: toString() : {
    
} 
```
