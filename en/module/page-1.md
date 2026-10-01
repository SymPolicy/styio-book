> **Historical design note, not current usage guidance.** This page preserves early proposals and rationale; code may be retired or never implemented. Start at the [current guide](../README.md) and do not infer active syntax or APIs from this page.

# Domain

```
// define a domain with name of "main"
[ `module` ] -> main := {
    `stmt`*
    `expr`
}

// if the domain is anonymous
// | is directly executed -> take as the entrance of program 
                           | and ignore any other domain behind the anonymous domain 
// | is imported from module -> ignore it
[ `module` ] -> {
    `stmt`*
    `expr`
}
```
