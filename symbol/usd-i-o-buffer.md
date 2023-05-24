# $ (I/O Buffer)

## Hello, World! <a href="#firstheading" id="firstheading"></a>

```
$: "Hello, World!"
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
