.PHONY: setup grpc

VENV_PATH := ./venv
PROTO_PATH := ./protos
PROTO_FILE := $(PROTO_PATH)/idverification.proto
SOURCE_FILES_PATH := ./src

# Default target
all: setup grpc

# Setup the environment
setup:
	@echo "Activating virtual environment and installing dependencies..."
	. $(VENV_PATH)/bin/activate; \
	pip install -r requirements.txt

# Generate gRPC files
grpc:
	@echo "Generating gRPC files..."
	@ $(VENV_PATH)/bin/activate; \
	python -m grpc_tools.protoc -I$(PROTO_PATH) --python_out=./src/. --pyi_out=./src/. --grpc_python_out=./src/. $(PROTO_FILE)

# Clean up generated files
clean:
	@echo "Cleaning up generated files..."
	@rm -f *_pb2.py *_pb2_grpc.py *.pyi

run_server: 
	@echo "starting the server"
	python $(SOURCE_FILES_PATH)/server.py

run_client:
	@echo "starting the client" 
	python $(SOURCE_FILES_PATH)/client.py
