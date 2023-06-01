# Dictionary

#### Styio Native

```
@(k, v) -> D >> {
    ...
}
```

#### Sugar <- Ruby Style

```
// k : key
// v : value

D >> { |k, v|
    ...
}

// x : tuple
// x[0] : key
// x[1] : value

D >> { |x|
    ...
}
```

#### Sugar <- "Evil" Style

```
D(k, v) >> {
    ...
}
```
