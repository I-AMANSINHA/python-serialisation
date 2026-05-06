import json
import base64

def data_converter():
    print("--- Python Data Converter ---")
    
    # 1. GET INPUT (Simulating a simple data object)
    user_name = input("Enter a name: ")
    user_age = input("Enter an age: ")
    
    # We put this into a Python Dictionary (Object)
    user_object = {
        "name": user_name,
        "age": int(user_age) if user_age.isdigit() else user_age,
        "app": "Converter",
        "status": "active"
    }
    
    print(f"\n[1] Original Python Object: {user_object}")

    # 2. SERIALIZATION (Object -> JSON String)
    serialized_json = json.dumps(user_object)
    print(f"[2] Serialized (JSON): {serialized_json}")

    # 3. ENCODING (String -> Base64)
    encoded_base64 = base64.b64encode(serialized_json.encode('utf-8')).decode('utf-8')
    print(f"[3] Encoded (Base64): {encoded_base64}")

    print("\n--- Reverse Process ---")

    # 4. DECODING (Base64 -> JSON String)
    decoded_json = base64.b64decode(encoded_base64).decode('utf-8')
    print(f"[4] Decoded back to JSON: {decoded_json}")

    # 5. DESERIALIZATION (JSON String -> Python Object)
    final_object = json.loads(decoded_json)
    print(f"[5] Deserialized back to Object: {final_object}")
    
    print(f"\nSuccess! The name inside the final object is: {final_object['name']}")

if __name__ == "__main__":
    data_converter()

