# BrainFuck

```
// read code file
code <- @("code.txt")

// create map for [ ]
map = []

// index of loop [ ]
iloop = 0

// last index of code text
ilast = |code| - 1

// match [ ] pairs
[0..ilast] >> #l ?= '[' :) {
    // found a loop
    iloop += 1
    
    // successfully matched the matched ']' or not
    success = $F
        
    // count backward
    count = 0
        
    // match backward
    [ilast..0] >> #r ?= ']' :) {
        count += 1
            
        ?(count == iloop) 
        :) {
            map ]+ (l, r)

            success = $T
                    
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        }
    }
    
    ?(success) :( {
        !!! <- $"For `[` at position {l}, the corresponding `]` was not found."
    }
}

// create memory
mem: i32[30000] = [0..]

// pointer location (index) in memory
ptr = 0

// character location (index) in code text
loc = 0

[...] >> code[loc] ?= {
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
            
            loc += 1
        }
    }
            
    "]" => {
        ? (mem[ptr] == 0) 
        :) {
            ptr = ptr + 1
            
            loc += 1
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
