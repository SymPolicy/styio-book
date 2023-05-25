# @

The `@` symbol is usually followed by a resource identifier.

```
@("https://styio.org");
```

Defining variables means bringing resources into the scope of the current code.

```
@(x, y);
```

Styio's resource identifier can be:

1. External Package
2. External URL Link
3. Variable
4. Function
5. Struct Type
6. Trait Type

### Read

#### => Mutable

```
@(d) <- @("./data.json"); // Comprehensive

@(d <- "./data.json"); // Recursive
```

#### => Immutable

```
d := <- @("./data.json");
```

### Write

```
d -> @("./data.json");
```
