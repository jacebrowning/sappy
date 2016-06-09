# sappy

Single-page application server for end-to-end testing.

Unix: [![Unix Build Status](http://img.shields.io/travis/jacebrowning/sappy/develop.svg)](https://travis-ci.org/jacebrowning/sappy) Windows: [![Windows Build Status](https://img.shields.io/appveyor/ci/jacebrowning/sappy/develop.svg)](https://ci.appveyor.com/project/jacebrowning/sappy)<br>Metrics: [![Coverage Status](http://img.shields.io/coveralls/jacebrowning/sappy/develop.svg)](https://coveralls.io/r/jacebrowning/sappy) [![Scrutinizer Code Quality](http://img.shields.io/scrutinizer/g/jacebrowning/sappy.svg)](https://scrutinizer-ci.com/g/jacebrowning/sappy/?branch=develop)<br>Usage: [![PyPI Version](http://img.shields.io/pypi/v/sappy.svg)](https://pypi.python.org/pypi/sappy) [![PyPI Downloads](http://img.shields.io/pypi/dm/sappy.svg)](https://pypi.python.org/pypi/sappy)

## Getting Started

### Requirements

* Python 3.4+

### Installation

Install `sappy` using pip:

```
$ pip install sappy
```

or directly from the source code:

```
$ git clone https://github.com/jacebrowning/sappy.git
$ cd sappy
$ python setup.py install
```

## Basic Usage

Build your static website (e.g. an Ember application) for production:

```
$ ember build --environment=production
Building...
Built project successfully. Stored in "dist/".
```

Then serve up the application:

```
$ sappy
Serving /home/browning/my_project/dist/ on 8080
```

Check out the [documentation](http://sappy.readthedocs.io/cli) or command-line help for additional options:

```
$ sappy --help
```
