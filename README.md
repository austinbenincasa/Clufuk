# Clufuk

A test program for sending a file with gRPC

## Requirements

- Python 3.6
- grpcio
- grpcio-tools
- googleapis-common-protos

## Building 
```
austin@computer:/Clufuk$ python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. .\fileTransfer.proto
```
