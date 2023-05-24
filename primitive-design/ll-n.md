# LL(n)

## Program

<pre><code>/*
 * A program can be 
 * either &#x3C;= { Dependency -> Space }
 * or &#x3C;= Block
 */
 
 Program :=
    &#x3C;= {
        (Dependency "->")? 
        
        Space
    }
    
<strong>    &#x3C;= Block
</strong></code></pre>

## Dependency

<pre><code>/*
 * Dependencies can be defined as a list of dependency items,
<strong> *     with the delimiter ","
</strong><strong> *   
</strong> * # ("abc", "xyz", ...)
 */
 
 Dependency := "(" DependencyItem ["," DependencyItem]* ~ ")"
</code></pre>

### Dependency Item

<pre><code>/*
<strong> * Dependency item must be [double quoted] [unix style path] string.
</strong> */
 
 DependencyItem := "path/to/package"
</code></pre>

## Space

```
/*
 * A space can be defined as
 *     and <= Global Variable Definition (one or none)
 *     and <= Global Function Definition (one or none)
 *     and <= Code Block (one or none)
 */

Space := 
    <= {
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
 
Expr := 
        <= FreeVarDef
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
