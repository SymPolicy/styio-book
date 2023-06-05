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

#### Only If Succeed (Guard)

```
x :) <- @("data.csv")
```
