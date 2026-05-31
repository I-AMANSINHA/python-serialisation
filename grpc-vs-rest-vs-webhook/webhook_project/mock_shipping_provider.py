import requests
import time

print("[Carrier] Simulating package transit...")
time.sleep(2) # Simulating time passing

webhook_url = "http://localhost:8000/webhook/shipping"
update_payload = {
    "tracking_id": "XYZ123456",
    "status": "Out for Delivery"
}

# The carrier triggers your webhook endpoint
response = requests.post(webhook_url, json=update_payload)
print(f"[Carrier] Webhook sent. Receiver responded with: {response.status_code}")

