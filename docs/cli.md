# Options

## Root Directory

The server will attempt to run in one of the following directories:

- `./dist`
- `./site`
- `./_site`
- `./public`
- `./`

To serve from a custom location:

```
$ sappy my/build/folder
```

## Custom Port

The default port is 8080. To use a custom port:

```
$ sappy --port 4200
```

# Actions

To open the site's index automatically:

```
$ sappy --launch
```
