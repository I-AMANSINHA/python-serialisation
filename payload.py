import json
import base64
import requests

# STEP 1: The Data
user_name = input("Enter a name: ")
user_age = input("Enter your age: ")

data = {"name": user_name, "age": user_age, "is_learning": True}
print(f"Step 1 (Object): {data}")

# STEP 2: Serialize
json_str = json.dumps(data)
print(f"Step 2 (JSON String): {json_str}")

# STEP 3: Encode
encoded_str = base64.b64encode(json_str.encode()).decode()
print(f"Step 3 (Base64 Safe): {encoded_str}")

# STEP 4: Send (The API Call)
url = " https://jsonplaceholder.typicode.com/posts"
payload = {"my_data": encoded_str}
response = requests.post(url, json=payload)

print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.json()}")
