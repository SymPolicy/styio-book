# Struct & Trait

## Struct

#### Styio Native

```
@(x: float, y: float) -> @Point

@Point <- @(x: float, y: float)

@Point <- (x: float, y: float)

@Point(x: float, y: float)
```

#### Sugar

```
@Point(x: float, y: float)
```



```
Person(name, addr) <: (Eq, Add, Mul) := {
    name :: {
    
    }
    
    Eq :: {
    
    }
    
    Add :: {
    
    }
    
    #? + (x) {
        
    }
    
    - #? {
    
    }
}
```

```
Person :: {
    name :: {
        
    }
    
    addr :: {
        
    }

    getAddr() := {
        
    }
    
    getName() := {
    
    }
}
```
