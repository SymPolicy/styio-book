# Resources

Read File

```
@(data: json <- "/path/to/file")
```

Write File

```
@(data -> "/path/to/file")
```

Network I/O - Download

```
@(data: json <- "http://path/to/file")
```



#### File

{% code fullWidth="false" %}
```
@("/path/to/a/directory/").walk()
    .forEach { entry ->
        if (entry.isfile()) {
            data = entry.read()
                .tojson()
                .filter(data["name"] == "Alice")
                .sendto("127.0.0.1:8888")
        }
    }

@("/path/to/a/directory/")
    >> (entry) 
    ? (entry.isfile()) 
    => { 
        data: json <- entry 
        ? (data["name"] == "Alice") 
            => { data -> @("127.0.0.1:8888") }
    }
    
        
@("/path/to/a/directory/")
    >> (entry) 
    ? (entry.isfile()) 
        => (data: json <- entry)
    ? (data["name"] == "Alice")
        => { data -> @("127.0.0.1:8888") }
```
{% endcode %}

1. get the resource address (anonymous)
2. parse -> found: this is a directory

step 2 can be skipped, if the type of resource has been provided, in some way

```
@dir("/path/to/a/directory/")
```

3. create an iterator for the directory

the iterator should not be invalidated even if some files are removed

4. and there is a filter, for each entry
5. read the file (entry)
6. and auto parse it to json

if there are other formats, just ignore them

if there are something wrong, just ignore them too

if there are something wrong, and we want to handle that, then

```
@("/path/to/a/directory/")
    >> (entry) ? (entry.isfile())
    => (data: json <- entry) ?= {
        !! => { >_($"Error: Failed to parse {entry.name} as json") }
        __ => {
            // Success
        }
    }
```

match regex: recognize link / file path

iterator: for each entry

recognize data format

load file

(deserialize) parse json to object / data struct

done

### Implementation

1.  build a regex analyzer to recognize type of resources:

    \[ file | directory | http / https | ftp | ... ]
2. implement an iterator over a directory tree, where each entry is a file (or directory) handler. And also choose the way of iteration (bfs / dfs).
3. find a way to call a function of an object
4. support: define a function and hence call the function
5. auto detect the data format of a file
6. auto parse json file

<pre><code>@("/path/to/a/directory/")
    >> (entry) 
    ? (entry.isfile()) 
        => (data: json &#x3C;- entry)
<strong>        => @(data: json &#x3C;- entry)
</strong><strong>        => #(data: json &#x3C;- entry)
</strong><strong>        => { data: json &#x3C;- entry }
</strong>    ? (data["name"] == "Alice") 
        => { data -> @("127.0.0.1:8888") }
</code></pre>

they act exactly the same,

but the meanings are different

`=> @(data: json <- entry)` is a resource initialization

`=> #(data: json <- entry)` is a template where data is given a default value

`=> { data: json <- entry }` is a statement that created a variable

more, it can also be `=> (data: json <- entry)`

this is a tuple, and there is an variable initialization in it

the tuple is anonymous, so it will be regarded as a collection of variables

an anonymous collection of variables can be acccessed by the lower layer in the chain which follows this collection

```
(data: json <- entry) 
    => { /* this is a lower layer */ } 
    => { /* another lower layer */ }
    => { /* lower *?}
```

the key is the following expression, but not previous expressions

`? (data["name"] == "Alice")` this expression is a closure

it can access to variables and resources in the upper layers which includes everything defined throughout the chain

well, the chain, is unlimited

the top layer of the chain, is not the chain

the chain contains everything which is defined in the domain of the chain

but each layer can only access to the upper layers that are defined ahead of the current layer

the lower layer is a closure

which introduces new variables and resources, but not affect upper layers

the chain is a stack in memory concern

you may access to a resource after a chain finished

but not anything in the middle

suppose a variable is defined by the top layer and be changed many time throughout the chain

if you are outside the chain

you can only see the result of the last modification

but you can never see any intermediate step

so, a chain, is actually a function

wonderful, we got a function

but a more flexible function

that support a chain of data processing

why do we need such a chain?

the chain supports predicate push down

we push down the filter to json parsing

while parsing json, we check the tag name

like `data["type"]`, we directly check tag of type.

as for those before the `type`, we skip them, but not parse them.

it sounds like how simdjson parse json

they record the positions of start and end symbols

like a string, there are two `"` at both the start and the end

we can directly skip over the string, and it will be super fast

if we found the target tag at a very early stage, there will be an early stop



skip over useless tags

early stop

what else?



twitter.json - simdjson - 2.4GB/s

\~1.5 cycles per byte

| simd-json                 | styio                                |
| ------------------------- | ------------------------------------ |
| read all of the content   | read only expected tags (early stop) |
| check if it is valid JSON | does not care at all                 |
| check unicode encoding    | check unicode encoding               |
| parse numbers             | parse numbers                        |
| build DOM                 | just a struct of data                |

simd-json

1.  avoid hard-to-predict branches

    each time a processor see a branch, it do branch predictions, so, remove branches where possible
2. use wide words (don't process byte by byte) -> SIMD
3. avoid memory allocation
4. measure the performance - benchmark driven development

Examples

1. UTF-8 -> only a very small part of unicode is valid character, so check bytes
2. detect escapable characters
3. get json structure by bitwise operation
4. number parsing is expensive

runtime dispatch -> pointer re-assignment

### Resource Types

#### Structured Data Formats

* json
* csv
* xml
* html
* toml
* yaml

#### Image Formats

* jpg, jpeg
* png
* webp
