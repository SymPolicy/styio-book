# BrainFuck

```
@mem: [30000] = [0..]

@ptr = 0

[...] >> {
    next <- >_()
    
    next ?= {
        ">" => {
            ptr = ptr + 1
        }
        
        "<" => {
            ptr = ptr - 1
        }
        
        "+" => {
            mem[ptr] = mem[ptr] + 1
        }
        
        "-" => {
            mem[ptr] = mem[ptr] + 1
        }
        
        "[" => {
            ? (mem[ptr] != 0) 
            :) {
                
            }
            :( {
                
            }
        }
        
        "]" => {
            
        }
        
        "," => {
            mem[ptr] <- >_()
        }
        
        "." => {
            mem[ptr] -> >_()
        }
    }
}
```
