# >> (Import)

## Variable

#### >> Block

Import unassigned variable into a code block.

```
@(x <int> = 0, y <float> = 0.0) >> { ... }
```

\* The **types** of variables can be&#x20;

&#x20;   either => **declared in the definition**&#x20;

&#x20;   or => **automatically inferenced in the block.**

\*\*&#x20;

\*\* _Warning: The unassigned variable \`x\` is never used and is therefore discarded._

#### >> Function

Define local variables which only live in the scope of a function.

```
@(x, y) >> f := {
    ...
}
```



## Dependency

1. Import external packages (dependencies) into a code space.

```
("math", "time") >> { ... }
```
