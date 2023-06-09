# BrainFuck

```
@mem_size = 30000

@mem: Array[mem_size] = [0..]

@ptr = 0

@iloop = 0

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
            iloop = iloop + 1
    
            ? (mem[ptr] == 0) 
            :) {
                ptr = ptr + 1
            }
            :( {
                count = 0
                [-mem_size..0] >> #(rptr) ?= {
                    "]" => {
                        count = count + 1
                            
                        ?(count == iloop) 
                        :) {
                            ptr = rptr
                                
                            ! >> ~;
                        }
                    }
                        
                    _ => ...
                }
            }
        }
        
        "]" => {
            ? (mem[ptr] == 0) 
            :) {
                ptr = ptr + 1
            }
            :( {
                count = 0
                [0..mem_size] >> #(lptr) ?= {
                    "]" => {
                        count = count + 1
                            
                        ?(count == iloop) 
                        :) {
                            ptr = lptr
                                
                            ! >> ~;
                        }
                    }
                        
                    _ => ...
                }
            }
        }
        
        "," => {
            mem[ptr] <- >_()
        }
        
        "." => {
            mem[ptr] -> >_()
        }
        
        _ => ...
    }
} 
```
