# Binding

`=` binds or rebinds a mutable value. `:=` creates a final binding. `:` supplies a type annotation, and `<-` is a resource/task transfer form rather than a general-purpose inference declaration. `#` marks a callable binding.

Final bindings and immutable container contents are different questions: a final list handle can still participate in accepted element-update operations. Use the selected compiler's [binding feature](https://github.com/Unka-Malloc/styio-nightly/blob/fd3b3e2d9a900fa58bc70641a42885c991650210/docs/design/syntax/features/core-final-and-mutable-binding.md) and [current guide](../current-language.md).
