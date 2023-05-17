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
