# I/O

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
