import grpc
from concurrent import futures
import inventory_pb2
import inventory_pb2_grpc

class InventoryService(inventory_pb2_grpc.InventoryServicer):
    def CheckStock(self, request, context):
        print(f"[gRPC Server] Checking stock for item: {request.item_id}")
        # Mock database lookup
        return inventory_pb2.StockResponse(in_stock=True, quantity=42)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    inventory_pb2_grpc.add_InventoryServicer_to_server(InventoryService(), server)
    server.add_insecure_port('[::]:50051')
    print("gRPC Server running on port 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()

