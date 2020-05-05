## Zserio Service using RPC via HTTP
Implementation of a zserio service using HTTP for remoting, written in **Python**.
zserio doesn't enforce any specific technology for remoting/RPC but provides 
a starting point to plugin different implementations easily. Have also a look at 
the other available examples and/or consider using [zswag](https://github.com/Klebert-Engineering/zswag)
to further ease application development.

## Package Structure
```bash
+-- myservice: Contains server and client apps 
   +-- zs: zserio schema and API generation logic 
   +-- http_rpc: HTTP based remoting for zserio generated service APIs
```

## Usage
Use `pip3` to install all needed dependencies:
```bash
pip3 install -r requirements.txt
```
Use server and client modules to actually run the example:
```bash
# Starting the server (using localhost:5000)
# Press Ctrl+C to quit it
python3 -m myservice.server 

# Starting the client
# Just follow the displayed instructions
python3 -m myservice.client
```
