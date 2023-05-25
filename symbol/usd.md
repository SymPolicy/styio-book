# $

## Hello, World! <a href="#firstheading" id="firstheading"></a>

`$:()` is a substitution of `print()`, which prints the given expression to `stdout`

```
$: ("Hello, World!")
```

## Standard IO

### Read

#### => Mutable

```
@(d) <- $("./data.json");
```

#### => Immutable

```
d := <- $("./data.json");
```

#### Write

```
d -> $("./data.json");
```
