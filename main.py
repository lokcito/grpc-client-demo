import grpc
import protos.contract_pb2_grpc as pb2_grpc
import protos.contract_pb2 as pb2


class GrpcClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self, host):
        self.host = host  # Use the CodeSandbox URL here

        # instantiate a channel
        self.channel = grpc.insecure_channel(self.host)

        # bind the client and the server
        self.stub = pb2_grpc.EquisDeStub(self.channel)

    def get_url(self, message):
        """
        Client function to call the rpc for GetServerResponse
        """
        message = pb2.MessageRequest(message=message)
        print(f"{message}")
        return self.stub.Ping(message)


if __name__ == '__main__':
    # Replace with the actual CodeSandbox URL
    client = GrpcClient('0.0.0.0:50051')
    result = client.get_url(message="Hello Server you there?")
    print(f"{result}")