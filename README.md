# Zserio Service HTTP backend

[![](https://github.com/ndsev/zserio-service-http-python/actions/workflows/build_linux.yml/badge.svg)](https://github.com/ndsev/zserio-service-http-python/actions/workflows/build_linux.yml)
[![](https://github.com/ndsev/zserio-service-http-python/actions/workflows/build_windows.yml/badge.svg)](https://github.com/ndsev/zserio-service-http-python/actions/workflows/build_windows.yml)
[![](https://img.shields.io/github/watchers/ndsev/zserio-service-http-python.svg)](https://GitHub.com/ndsev/zserio-service-http-python/watchers)
[![](https://img.shields.io/github/forks/ndsev/zserio-service-http-python.svg)](https://GitHub.com/ndsev/zserio-service-http-python/network/members)
[![](https://img.shields.io/github/stars/ndsev/zserio-service-http-python.svg?color=yellow)](https://GitHub.com/ndsev/zserio-service-http-python/stargazers)

--------

Sample implementation of Zserio Service HTTP backend in **Python**.

# Prerequisites

1. Java JRE 8+
1. Python 3.8+
1. Web framework flask:

   ```
   python3 -m pip install flask
   ```
1. Zserio compiler with Python runtime library:

   ```
   python3 -m pip install zserio
   ```

# Usage

## Calculator Example

```bash
cd examples/calculator
# generate service using Zserio
zserio calculator.zs -python ../../build/gen

export PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH=../../src:../../build/gen
python3 calculator_server.py &
python3 calculator_client.py
# follow client's instructions
# ...
# press q + ENTER to quit the client
fg
# press Ctrl+C to quit the server
```
