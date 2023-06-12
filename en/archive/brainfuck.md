# BrainFuck

```
// read code file
code <- @("code.txt")

// create map for [ ]
map = []

// index of loop [ ]
iloop = 1

// match [ ] pairs
[0..|code|] >> #(l) => {
    ?(code[l] == '[')
    :) {
        // found or not
        found = $F
        
        // count backward
        count = 0
        
        // reversed code text
        rev_code = code[<<]
        
        // match backward
        rev_code >> #r ?= ']' :) {
            count += 1
            
            ?(count == iloop) 
            :) {
                map ]+ (l, code[?= r])

                found = $T
                    
                ^^^^^^^^^^^^^^^^^^^^^^
            }
        }
        
        ?(found)
        :) {
            iloop += 1
        } 
        :( {
            !!! ($"Error: For the `[` at position {l}, the corresponding `]` is not found.")
        }
    }
}

// create memory
mem: i32[30000] = [0..]

// pointer location (index) in memory
ptr = 0

// character location (index) in code text
loc = 0

[...] >> #(code[loc] -> char) ?= {
    ">" => {
        ptr = ptr + 1
            
        loc += 1
    }
            
    "<" => {
        ptr = ptr - 1
            
        loc += 1
    }
            
    "+" => {
        mem[ptr] = mem[ptr] + 1
            
        loc += 1
    }
            
    "-" => {
        mem[ptr] = mem[ptr] - 1
            
        loc += 1
    }
        
    "," => {
        mem[ptr] <- >_()
            
        loc += 1
    }
            
    "." => {
        mem[ptr] -> >_()
            
        loc += 1
    }
            
    "[" => {
        ? (mem[ptr] == 0) 
        :) {
            map >> #(i, j) => {
                ?(i == loc)
                :) {
                    loc = j
                }
            }
        }
        :( {
            ptr = ptr + 1
        }
    }
            
    "]" => {
        ? (mem[ptr] == 0) 
        :) {
            ptr = ptr + 1
        }
        :( {
            map >> #(i, j) => {
                ?(j == loc)
                :) {
                    loc = i
                }
            }
        }
    }
            
    _ => {
        loc += 1
    }
} 
```
