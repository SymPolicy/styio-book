# Variable

### Define

```
@(x, y);
```

### Define + Assign&#x20;

#### Mutable =>

```
/*
 * Recursive Assignment
 * 1. Define `x`.
 * 2. Initialize `x` = 1.
 * 3. Define `y`.
 * 4. Initialize `y` = 2.
 */
 
@(x = 1, y = 2);

/*
 * Comprehensive Assignment
 * 1. Define `x` and `y`.
 * 2. Set `x` as 1
 * 3. Set `y` as 2
 */
 
@(x, y) = (1, 2);

/*
 * Adaptive Transformation (<~)
 * 1. Define `x` and `y`.
 * 2. Define a tuple (1, 2)
 * 3. Deconstruct (1, 2)
 * 4. Deconstruct (x, y)
 * 5. Map x to 1
 * 6. Map y to 2
 */
 
@(x, y) <~ (1, 2);
```

#### Immutable =>

When a variable has been assigned once using walrus symbol :=, it will become immutable.

```
@(x, y) := (1, 2);
```

### Define

#### + Type =>

```
@(x: int = 0)
```

#### + Optional Type =>

```
@(x: [int|float])
```
