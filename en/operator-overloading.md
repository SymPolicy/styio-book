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
@(x, y) -> Point : {
    ...
}

// Nested Define and Implementation
@Point(x, y): {
    x : {
        $x 
    }
    
    y : {
        $y
    }

    // Negative
    - $Point : {
    
    }
    
    // Addition
    $Point + @(y) : {
    
    }
    
    // Reversed Addition
    @(y) + $Point : {
    
    }
    
    // Incremental Addition
    $Point += @(y) : {
    
    }
}

// Additional Function Define And Implementation
Point +: toString() : {
    
} 
```
