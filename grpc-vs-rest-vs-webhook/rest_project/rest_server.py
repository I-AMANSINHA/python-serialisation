from flask import Flask, request, jsonify

app = Flask(__name__)

# Virtual Database
users_db = {
    1: {"name": "Alice", "role": "Developer", "status": "active"},
    2: {"name": "Bob", "role": "Designer", "status": "pending"}
}

# 1. GET - Read/Retrieve data
@app.route('/users', methods=['GET'])
def get_users():
    print("[API Server] GET request received - Fetching all users")
    return jsonify(users_db), 200

# 2. POST - Create brand new data
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_id = max(users_db.keys()) + 1
    users_db[new_id] = {
        "name": data.get("name"),
        "role": data.get("role"),
        "status": "active"
    }
    print(f"[API Server] POST request received - Created user #{new_id}")
    return jsonify({"message": "User created", "user_id": new_id}), 201

# 3. PUT - Replace an entire resource completely
@app.route('/users/<int:user_id>', methods=['PUT'])
def replace_user(user_id):
    if user_id not in users_db:
        return jsonify({"error": "User not found"}), 404
    
    data = request.json
    # Overwriting the entire object. If a field is missing, it disappears.
    users_db[user_id] = {
        "name": data.get("name"),
        "role": data.get("role"),
        "status": data.get("status") # Must explicitly provide everything
    }
    print(f"[API Server] PUT request received - Replaced entire user #{user_id}")
    return jsonify({"message": "User fully replaced", "user": users_db[user_id]}), 200

# 4. PATCH - Partially update an existing resource
@app.route('/users/<int:user_id>', methods=['PATCH'])
def partial_update_user(user_id):
    if user_id not in users_db:
        return jsonify({"error": "User not found"}), 404
    
    data = request.json
    # Only updates fields provided in the payload. Others remain untouched.
    if "name" in data: users_db[user_id]["name"] = data["name"]
    if "role" in data: users_db[user_id]["role"] = data["role"]
    if "status" in data: users_db[user_id]["status"] = data["status"]
    
    print(f"[API Server] PATCH request received - Updated specific fields for user #{user_id}")
    return jsonify({"message": "User fields patched", "user": users_db[user_id]}), 200

# 5. DELETE - Remove a resource
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users_db:
        return jsonify({"error": "User not found"}), 404
    
    deleted_user = users_db.pop(user_id)
    print(f"[API Server] DELETE request received - Removed user #{user_id}")
    return jsonify({"message": f"User #{user_id} deleted successfully"}), 200

if __name__ == '__main__':
    app.run(port=5000)

