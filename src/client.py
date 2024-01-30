from __future__ import print_function

import logging

import grpc
import idverification_pb2
import idverification_pb2_grpc


def image_verification_request_iter(message_bytes):
    for byte_ in message_bytes:
        yield idverification_pb2.VerificationImageRequest(
            chunk_data=byte_,
            image_info=idverification_pb2.ImageInfo(
                message_id="1",
                image_type="test_image_type",
                identification_type="test_identification_type",
            ),
        )


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.

    dummy_image_chunk_data = b"hello"
    p1 = dummy_image_chunk_data[:2]
    p2 = dummy_image_chunk_data[2:]
    image_chunks = image_verification_request_iter([p1, p2])
    # helloworld_pb2.VerificationImageInfo()

    with grpc.insecure_channel("localhost:8001") as channel:
        stub = idverification_pb2_grpc.IdVerificationStub(channel)
        image_response = stub.ImageVerificationRequest(
            image_chunks,
        )

    print(f"Got image response {image_response}")


if __name__ == "__main__":
    logging.basicConfig()
    run()
