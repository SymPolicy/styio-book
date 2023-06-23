---
description: Introduction to Styio Programming Language
---

# Styio

Styio is a symbol-only programming language, with the following features:

* **Resource Dispatch**. Styio is a symbolic representation of resources inputs, flows, transformations, and outputs. It is designed to deconstruct, reorganise, and compute large complex data warehouse. Styio operates on the basis of a mapping relationship between resource identifiers and instance data structures.&#x20;
* **Only symbols**. Styio uses well-defined, unambiguous symbols (``~! @#$%^&*()_+}{":? ><|`-=[];',. /``) instead of the keywords that are usually present in other programming languages (`def fn for while if else class struct ...` ).&#x20;
* **Symbolic Intuition**. Styio follows the conventions of other languages as much as possible, and conforms to the most basic intuitions. Styio avoids language-specific keywords whenever possible, so you won't see `def` or `fn`, you'll just see the resource `@` and the template `#`.&#x20;
* **Template comments**. The most common feature of Styio is the Template. Templates are defined using the `#` symbol, which in other languages usually means a comment. Through templates, the developer explicitly annotates the role of the compiler to other code maintainers while declaring it to the compiler.&#x20;
* **Turing Complete**. Styio has an official implementation of the BrainFuck interpreter.
