# Zserio Service HTTP backend

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
