# Primitive

```
// define 2 temporal variables `k` and `v`
@(k, v)

// push temporal variables into the domain of `R`
// since R is a dictionary
// `k` and `v` will be automatically cast to key and value of `R`
@(k, v) -> R

// send R to a loop
// R will be cast to an iterator
// operations in code block will apply to each element (key-value pair) of R
@(k, v) -> R -> [...] {
   // code block 
}
// the code block { `stmt`* `expr`* }
// can be simplified to | `expr` | 
// if there is one (and at most one) expression
// and no statements
@(k, v) -> R -> [...] | `expr` |

// the loop R[...]
// can be simplified as R...
@(k, v) -> R... | `expr` |

// simplify variables as function definition style
R(k, v)... | `expr` |
```
