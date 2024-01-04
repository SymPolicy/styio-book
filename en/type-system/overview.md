# Overview

### Numbers

Generally, the compiler chooses data type, so generic types are enough for type checking.

For generic types, we follow Python style, but not the same:

| Generic Type Name         |
| ------------------------- |
| Integer \| integer \| int |
| Float \| float            |
| Decimal \| decimal        |

But if you really want to do something with data types, here you go.

For specific types, we follow [Kotlin](https://kotlinlang.org/docs/basic-types.html) style, but not the same:

<table><thead><tr><th width="183">Type Name</th><th>Type Names</th></tr></thead><tbody><tr><td>Integer</td><td>Int8, Int16, Int32, Int64, Int128</td></tr><tr><td>Unsigned Integer</td><td>UInt8, UInt16, UInt32, UInt64, UInt128</td></tr><tr><td>Float</td><td>Float32</td></tr><tr><td>Double</td><td>Double, Float64</td></tr></tbody></table>

### String

String is a collection, which was treated the same as array and list.&#x20;

| Type Name               |
| ----------------------- |
| String \| string \| str |
