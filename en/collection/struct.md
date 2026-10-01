> **Historical design note, not current usage guidance.** This page preserves early proposals and rationale; code may be retired or never implemented. Start at the [current guide](../README.md) and do not infer active syntax or APIs from this page.

# Struct

```
Point := (
    x: float, 
    y: float
)

O = Point(
    x = 0.0,
    y = 0.0
)

I = Point(
    x = 1.0,
    y = 1.0
)

Person(name, addr) <: (Eq, Add, Mul) := {
    name :: {
    
    }
    
    Eq :: {
    
    }
    
    Add :: {
    
    }
    
    #`$? + {x}` : {
        
    }
    
    #`- $?`: {
    
    }
}
```
