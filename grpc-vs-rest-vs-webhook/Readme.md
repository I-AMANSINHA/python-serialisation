<H1> gRPC V/S REST API V/S WEBHOOK </H1>

<p> gRPC </p>

- Use gRPC for the high-speed communication between your internal backend systems where low latency is critical.

- Scenario: Your frontend API needs to instantly verify if an item is in stock before letting a customer check out.

<p> REST API </P>

- Use a traditional REST API for the standard, public-facing action where a client explicitly requests a one-time change.

- Scenario: The customer clicks "Buy Now" on the checkout page, sending user data and payment details to the server.

<P> WEBHOOK </P> 

- Use a Webhook to let a third-party delivery service automatically notify your application when the status changes, without making your app constantly ask for updates.

- Scenario: The shipping carrier updates the package status to "Out for Delivery," which automatically alerts your main application.

<H1> Structure </H1>
grpc-vs-rest-vs-webhook/
│
-  README.md                       # Instructions on how to run everything
-  requirements.txt                # List of Python dependencies
│
- grpc_project/                 # gRPC Files
   ├── inventory.proto             # Protocol Buffer contract definition
   ├── inventory_pb2.py            # Generated automatically by protoc
   ├── inventory_pb2_grpc.py       # Generated automatically by protoc
   ├── grpc_server.py              # The running gRPC backend
   └── grpc_client.py              # Script to test the gRPC service

- rest_project/                 # REST API Files
   ├── rest_server.py              # Flask app with the /orders endpoint
   └── rest_client.py              # Script that sends the POST request

- webhook_project/              # Webhook Files
   ├── webhook_receiver.py         # Flask app waiting for external data
   └── mock_shipping_provider.py   # Script simulating the carrier event

Notes:- 
1. gRPC uses a .proto file to define the communication contract.

2. Run this command in your terminal to generate the gRPC code automatically:
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. inventory.proto

3. Have to run this files "grpc_server.py", "grpc_client.py", "rest_server.py", "rest_client.py", "webhook_receiver.py", "mock_shipping_provider.py" , in separate windows to check and test the workflow of these.

4. Use gRPC when: You are connecting server-to-server inside your own architecture, where you own both sides of the code and absolute speed is your top priority.

5. gRPC uses unary RPCs for standard requests. This is a strict "one request, one response"
