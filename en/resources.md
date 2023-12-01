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

```
@("/path/to/file").walk()
    .foreach()
    .tojson().as(data)
    .filter(data["name"] == "Alice")
    .sendto("127.0.0.1:8888")

@("/path/to/a/directory/")
    >> (entry)
    ? (entry.isfile())
    => (data: json <- entry)
    ? (data["name"] == "Alice") 
    => { data -> @("127.0.0.1:8888") }
```

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
