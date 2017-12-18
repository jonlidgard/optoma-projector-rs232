[![Build status][travis-image]][travis-url] 
[![Coverage percentage][coveralls-image]][coveralls-url]

# optoma-projector-rs232

A python class that communicates with Optoma Projector&#39;s over an RS232 serial link

## Requirements

- Python 3.5.2+

## Install

```
pip install git@github.com:jonlidgard/optoma-projector-rs232.git#egg=optoma-projector-rs232
```

## Develop

This package comes with a setup.sh script which swiftly
creates a virtualenv and installs dependencies from requirements.txt
without the hassle of virtualenv wrapper:

```
. ./setup.sh -p python3.5.2
```

## Test

```
py.test -v -s --cov-report term-missing --cov=optoma-projector-rs232 -r w tests
```

## License

[MIT](LICENSE) 2017 jonlidgard

[travis-image]: https://travis-ci.org/jonlidgard/optoma-projector-rs232.svg?branch=master
[travis-url]: https://travis-ci.org/jonlidgard/optoma-projector-rs232
[coveralls-image]: https://coveralls.io/repos/jonlidgard/optoma-projector-rs232/badge.svg
[coveralls-url]: https://coveralls.io/r/jonlidgard/optoma-projector-rs232
