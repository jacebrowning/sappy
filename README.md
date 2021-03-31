[![Unix Build Status](https://img.shields.io/github/workflow/status/jacebrowning/sappy/main?label=unix)](https://github.com/jacebrowning/sappy/actions?query=branch%3Amain)
[![Windows Build Status](https://img.shields.io/appveyor/ci/jacebrowning/sappy/main.svg?label=window)](https://ci.appveyor.com/project/jacebrowning/sappy)
[![Coverage Status](http://img.shields.io/coveralls/jacebrowning/sappy/main.svg)](https://coveralls.io/r/jacebrowning/sappy)
[![Scrutinizer Code Quality](http://img.shields.io/scrutinizer/g/jacebrowning/sappy.svg)](https://scrutinizer-ci.com/g/jacebrowning/sappy/?branch=main)
[![PyPI Version](http://img.shields.io/pypi/v/sappy.svg)](https://pypi.python.org/pypi/sappy)

# Overview

Sappy is a simple, single-page application (SPA) web server for end-to-end testing.

The Python standard library includes a web server that works great for serving up files:

```sh
$ python3 -m http.server 8080
Serving HTTP on 0.0.0.0 port 8080 ...

$ curl http://localhost:8080/index.html
<!DOCTYPE html>
<html>
  <head>
    <title>Example Index</title>
...
```

But when used to serve up single-page applications, a `404` is returned whenever any page other than the index is accessed directly:

```sh
$ curl http://localhost:8080/login
<!DOCTYPE html>
<html lang=en>
  <title>Error 404 (Not Found)</title
...
```

This project builds on the existing web server code to forward all requests to the index. The single-page application’s client-side routing can then display the page that corresponds to that request’s URL.

# Setup

## Requirements

* Python 3.6+

## Installation

Install `sappy` with pip:

```sh
$ pip install sappy
```

or directly from the source code:

```sh
$ git clone https://github.com/jacebrowning/sappy.git
$ cd sappy
$ python setup.py install
```

# Usage

Build your static website (e.g. an Ember application) for production:

```sh
$ ember build --environment=production
Building...
Built project successfully. Stored in "dist/".
```

Then serve up the application:

```sh
$ sappy
Serving /home/browning/project/dist/ on 8080
```

Check out the [documentation](http://sappy.readthedocs.io/en/latest/cli) or command-line help for additional options:

```sh
$ sappy --help
```
