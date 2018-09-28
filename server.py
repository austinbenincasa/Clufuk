import concurrent.futures
import fileTransfer_pb2
import fileTransfer_pb2_grpc
import grpc
import time

class FileReceiver(fileTransfer_pb2_grpc.FileSendServicer):
    def SendChunk(self, request_iterator, context):
        count = 0
        filename = "big_recv.txt"
        file = open(filename, "w")
        for request in request_iterator:
            count += 1
            file.write(request.chunk)
        file.close()
        print(f"Received file with {count} lines")
        return fileTransfer_pb2.ChuckReceived(reply=count)

def main():
    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
    fileTransfer_pb2_grpc.add_FileSendServicer_to_server(FileReceiver(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(60*60*24)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    main()