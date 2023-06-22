# List

```
[0, 1, 2, ...]
```

## Range

```
// start: inclusive
// end: exclusive

[start..end]
```

```
// reversed list

x = << [0, 1, 2]

// [2, 1, 0]
```

```
@memory = []

// push 
memory ]+ 0

// drop the last element
memory ]-

// insert to the first element
memory [+ 0

// drop the first element 
memory [-

// List Formation
/*
 How to read this?
 1. See [], so `a` is a List.
 2. See <<, so this is a filling operation
 3. See (k, v), so we are iterating over a Dict.
 4. See ==(v)==, we only need `v`.
 
 It is easy to read, and more expressive.
 */

a = [] << {
  d >> (k, v) => {
    ==(v)==
  }
}

// Comprehensive
a = [d ~> (k, v) => v]

a = list(d.values())

// Iteration
a = [d >> (k, v) => v]

a = [v for k, v in d]
```
