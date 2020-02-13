# Zserio Service HTTP backend

Sample implementation of Zserio Service HTTP backend in **Python**.

# Prerequisites

   1. Python 3 with flask installed

      ```bash
      python3 -m pip install flask
      ```

   2. Zserio Python runtime library
   3. Zserio compiler (`zserio.jar`)

> Zserio prerequisites are included in this repo in 3rdparty folder.

# Usage

## Calculator Example

```bash
cd examples/calculator
# generate service using Zserio
java -jar ../../3rdparty/zserio.jar calculator.zs -python gen

export PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH=../../3rdparty/runtime:../../src:gen
python3 calculator_server.py &
python3 calculator_client.py
# follow client's instructions
# ...
# pres q + ENTER to quit the client
fg # and pres Ctrl+C to quit the server
```
