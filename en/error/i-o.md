# I/O

### Error Handle

#### => Now.&#x20;

```
x | :) <- @("data.csv")
  | :( {
    >_ ("Error: Failed.")
}
```

#### => Later. Keep the error.

```
x :? <- @("data.csv")

...


x ?= {
    // Value Case
    :) => {
        ...
    }
    
    // Error Case
    :( => {
        ...
    }
    
    // Note: You don't need to specify the default case.
    // since happy guard :) and sad guard :( are enumerate of guard type.
}
```

#### Error Handling

Manually handle cases&#x20;

success: assign

fail: print message

```
x | :) <- @("data.csv")
  | :( {
    >_ ("Error: Failed.")
  }
```

#### Force Assign

If fails, then the program crashes.

```
x <- @("data.csv")
```

#### Uncertain value

x can be a value or an error.&#x20;

```
x :? <- @("data.csv")
```
