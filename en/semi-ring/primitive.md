# Primitive

```
// define 2 temporal variables `k` and `v`
@(k, v)

// bring variables `k` and `v` into the scope of `R`
// since R is a dictionary
// `k` and `v` will be automatically cast to key and value of the dictionary
@(k, v) -> R

// send R to a loop
// R will be cast to an iterator
// operations in code block will apply to each element (key-value pair) of R
@(k, v) -> R ~> [...] >> {
   // code block 
}

// the code block { `stmt`* `expr`* }
// can be simplified to | `expr` | 
// if there is one (and at most one) expression
// and no statements
@(k, v) -> R ~> [...] >> | `expr` |

// the loop R[...]
// can be simplified as R...
@(k, v) -> R... | `expr` |

// simplify variables as function definition style
R(k, v)... | `expr` |

// add a default operator (aggregation function)
@(k, v) -> sum(R) | `expr` |

// bring temporal variables into aggregation
// means "decompose R, iterate each element as <k, v> pair"
sum(R, <k, v>) | `expr` |
```

```
(x x): "[ERROR]: ..."
(! !): "[WARN ]: ..."
(> <): "[INFO ]: ..."
```
