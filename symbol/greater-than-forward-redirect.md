---
description: Load external resources and redirect to the right.
---

# -> (Forward Redirect)

## Variable

#### >> Block

Import unassigned variable into a code block.

```
@(x: int = 0, y: float = 0.0) -> { ... }
```

\* The **types** of variables can be&#x20;

&#x20;   either => **declared in the definition**&#x20;

&#x20;   or => **automatically inferenced in the block.**

\*\* _Warning: The unassigned variable \`x\` is never used and is therefore discarded._

#### >> Function

Define local variables which only live in the scope of a function.

```
@(x, y) -> f := {
    ...
}
```

## Dependency

#### >> Space

Import external packages (dependencies) into a code space.

<pre><code><strong>$(
</strong> "math", 
 "time",
) >> { ... }
</code></pre>

## OS Read/Write

#### Export to CSV file. (Auto Cast)

<pre><code><strong>data -> $("data.csv")
</strong></code></pre>
