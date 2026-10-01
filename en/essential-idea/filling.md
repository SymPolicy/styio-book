> **Historical design note, not current usage guidance.** This page preserves early proposals and rationale; code may be retired or never implemented. Start at the [current guide](../README.md) and do not infer active syntax or APIs from this page.

# Filling

\``#`\` means a template, which is the start of filling process. Variables labelled with `#` will be filled with a certain value later.

\``$`\` means a reference, which is the end of filling process. It searches the existing vairables in the scope and fill in a certain value.&#x20;

{% hint style="info" %}
The main reason of using `#()` as template is that it is actually a **comment** to make people understand what is going on here and reduce ambiguity!

For example, if you simply put two variables after an iteration, like `R >> k, v` the parser can understand what you want to do, but it is not clear with respect to readability. So you have to tell others with your code that there is a template of two variables, and you are going to fill it for each element of `R`.

This is a design forces you to comment, it is a strict limitation on the code writer.
{% endhint %}

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
