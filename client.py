import grpc
import time
import fileTransfer_pb2
import fileTransfer_pb2_grpc

def main():
    channel = grpc.insecure_channel('localhost:50051')
    stub = fileTransfer_pb2_grpc.FileSendStub(channel)
    start = time.time()
    response = stub.SendChunk(chunker())
    end = time.time()
    print(f"Took {str(end - start)} seconds to send {str(response.reply)} lines")


def chunker():
    filename = "big.txt"
    file = open(filename, "r")
    for line in file:
        yield fileTransfer_pb2.Chunk(chunk=line)
    file.close()

if __name__ == '__main__':
    main()
