# Filling

\``#`\` means a template, which is the start of filling process. Variables labelled with `#` will be filled with a certain value later.

\``$`\` means a reference, which is the end of filling process. It searches the existing vairables in the scope and fill in a certain value.&#x20;

#### Intuitive

\``#`\`(Template) are empty pigeon holes, waiting for pigeons to move in.

\``$`\`(Reference) are full-filled pigeon holes, there is a pigeon in each hole.

### Example

Iterate over `R`, for each element, split it and auto fill in the template `#(k, v)`, then execute single branch `=> { ... }`.

```
R >> #(k, v) => {
    ...
}
```
