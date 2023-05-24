# Example

### Variable

**Example 1.**&#x20;

Define a variable without assignment.

```
// "@" <ID>

@(x)
```

**Example 2.**&#x20;

Define multiple variables without assignment.

<pre><code><strong>// "@" "(" [&#x3C;ID> ["," &#x3C;ID>]*]? ")"
</strong>
@(x, y)
</code></pre>

### Function

**Example 1.**&#x20;

Define a function without arguments.&#x20;

```
// <ID> ":=" <DOMAIN>

f := { ... }
```

**Example 2.**&#x20;

Define a function with multiple arguments.

```
// [<VAR_DEF>]? [">>"]? <ID> ":=" <DOMAIN>

@(x, y) >> f := { ... }
```

**Example 3.**

Define an anonymous function with multiple arguments.

```
// [<VAR_DEF>]? [">>"]? <DOMAIN>

@(x, y) >> { x + y }
```

### Module

```
(
  " ",
  " ",
) >> `name` := {
  ...
}
```
