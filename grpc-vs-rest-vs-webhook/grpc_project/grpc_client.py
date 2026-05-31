import grpc
import inventory_pb2
import inventory_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = inventory_pb2_grpc.InventoryStub(channel)
        response = stub.CheckStock(inventory_pb2.StockRequest(item_id="item_99"))
    print(f"[gRPC Client] Response: In Stock={response.in_stock}, Qty={response.quantity}")

if __name__ == '__main__':
    run()

