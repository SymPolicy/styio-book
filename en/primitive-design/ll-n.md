# LL(n)

## Program

```
/*
 * A program can be 
 * either <= { Dependency -> Space }
 * or <= Block
 */
 
 Program :=
    | {
        (Dependency ">>")? 
        
        Space
    }
    
    | Block
```

## Dependency

```
/*
 * Dependencies can be defined as a list of dependency items,
 *     with the delimiter ","
 *   
 * @("abc", "xyz", ...)
 */
 
 Dependency := "@" "(" DependencyItem ["," DependencyItem]* ")"
```

### Dependency Item

```
/*
 * Dependency item must be [double quoted] [unix style path] string.
 */
 
 DependencyItem := "path/to/package"
```

## Space

```
/*
 * A space can be defined as
 *     and <= Global Variable Definition (one or none)
 *     and <= Global Function Definition (one or none)
 *     and <= Code Block (one or none)
 */

Space := 
    | {
        [VarDef]?
        [FuncDef]?
        [Block]?
    }
```

## Block

```
/*
 * A code block can be defined as 
 *     (optional) a sequence of statements 
 *     followed by (optional) a value expression as return.
 */
 
Block := [Stmt]* [Expr]?


```

## Statement

```
/*
 * A statement is just an expression ending with a simi-colon ";"
 */
 
 Stmt := Expr ";"
```

## Expression

```
/*
 * Everything is an expression.
 */
 
Expr := FreeVarDef
      | 
```

## Variable Definition

### Free Variable (Undefined)

```
FreeVarDef := "@" <ID>
            | "@" [<ID> ["," <ID>]*]?
            
            | "@" "(" <ID> ")"
            | "@" "(" [<ID> ["," <ID>]*]? ")"
```

### Variable (Assignment)

```
VarAssign := <ID> ":=" <EXPR>
```
