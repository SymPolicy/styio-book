# Runtime

standard library must be separated from runtime library.

standard library should takes common methods in libc.

runtime library is more or less related to the type system

we definitely don't need callback

choose between async+await and coroutine.

***

#### Computation

parallel

multi-threading

#### Concurrent Tasks

async+await or coroutine

async+await -> machine state

await: could be pending (or ready (then return))

coroutine:&#x20;



```
total_contribution_of_alice = @("file/path") >> #(f: json) ? {
    f.filter((o) => (o.name == "Alice"))
     .sum((o) => o.contribution)
}
```

`file: json` Assume the files ending with 'json' must be in the correct json format.

`filter` should accept a boolean expression, and implements an early-stop optimization

`sum` should accept columns expression, which also applies an early-stop optimization

the IR should contains at least the following information:

we only need two columns: "name" and "contribution"

we might need something like a DSL, and also an IR.

```
filter[name] => sum[contribution]
```

as you may have noticed, we need to record "sequential operations", in another word, "a chain of operations". Therefore, a linked list might be helpful.

steps: syscall (traverse directory and find file name, read file (bytes)), deserialization, filter, sum.&#x20;

syscall (reading file) is blocking, io\_uring is useful here.

deserialization: we only need two columns in this step, make purposeful match.

filter, sum: use SIMD and multi-threading to accelerate.
