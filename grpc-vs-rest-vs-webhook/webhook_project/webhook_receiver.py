from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook/shipping', methods=['POST'])
def shipping_webhook():
    payload = request.json
    print(f"\n🚨 [Webhook Received] Package Status Alert! 🚨")
    print(f"Tracking ID: {payload.get('tracking_id')}")
    print(f"New Status: {payload.get('status')}")
    return jsonify({"received": True}), 200

if __name__ == '__main__':
    app.run(port=8000)

