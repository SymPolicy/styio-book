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
    .forAll()
    .parse().as(data)
    .filter(data["name"] == "Alice")
    .sendTo("127.0.0.1:8080")
```

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
