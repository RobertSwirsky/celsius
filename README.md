# celsius project

[![PyPI - Version](https://img.shields.io/pypi/v/celsius.svg)](https://pypi.org/project/celsius)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/celsius.svg)](https://pypi.org/project/celsius)

-----

## Table of Contents

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install celsius
```
Be sure to add the following likes to your /boot/firmware/config.txt and reboot

```
# w1tempteraturesensor
dtoverlay=w1-gpio,pullup="y"
dtparam=spi=off
```

## License

`celsius` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
