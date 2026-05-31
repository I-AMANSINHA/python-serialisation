import requests
import json

BASE_URL = "http://localhost:5000/users"

def print_step(title):
    print(f"\n--- 🚀 {title} ---")

# Step 1: GET (Read original database)
print_step("Testing GET (Read)")
res = requests.get(BASE_URL)
print(f"Status: {res.status_code}\nData: {json.dumps(res.json(), indent=2)}")

# Step 2: POST (Create user #3)
print_step("Testing POST (Create)")
new_user = {"name": "Charlie", "role": "Manager"}
res = requests.post(BASE_URL, json=new_user)
print(f"Status: {res.status_code}\nData: {res.json()}")

# Step 3: PUT (Replace user #1 completely)
print_step("Testing PUT (Complete Overwrite)")
# Notice we change Alice to Alex and omit her 'status'. The server will overwrite everything.
overwrite_data = {"name": "Alex", "role": "Senior Dev", "status": "on_leave"}
res = requests.put(f"{BASE_URL}/1", json=overwrite_data)
print(f"Status: {res.status_code}\nData: {json.dumps(res.json(), indent=2)}")

# Step 4: PATCH (Partial Update to user #2)
print_step("Testing PATCH (Partial Update)")
# We ONLY want to change Bob's status to 'active'. His name and role should stay intact.
patch_data = {"status": "active"}
res = requests.patch(f"{BASE_URL}/2", json=patch_data)
print(f"Status: {res.status_code}\nData: {json.dumps(res.json(), indent=2)}")

# Step 5: DELETE (Remove user #3)
print_step("Testing DELETE (Remove)")
res = requests.delete(f"{BASE_URL}/3")
print(f"Status: {res.status_code}\nData: {res.json()}")

# Final Step: GET (Verify final state of the database)
print_step("Final Database State Verification")
res = requests.get(BASE_URL)
print(json.dumps(res.json(), indent=2))

