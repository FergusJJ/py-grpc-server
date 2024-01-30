import grpc
import logging
from concurrent import futures


import idverification_pb2
import idverification_pb2_grpc


class IdVerification(idverification_pb2_grpc.IdVerification):
    def ImageVerificationRequest(self, request, context):
        message_id = "1"
        message_length = 1
        print(f"received message: {request}")
        return idverification_pb2.VerificationImageResponse(
            message_id=message_id, message_length=message_length
        )


def serve():
    port = "8001"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    idverification_pb2_grpc.add_IdVerificationServicer_to_server(
        IdVerification(), server
    )
    server.add_insecure_port("127.0.0.1:" + port)

    server.start()
    print("server started on port " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
