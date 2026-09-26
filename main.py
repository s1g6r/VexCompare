import os, json, requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ.get("VEX_TOKEN")
if TOKEN is None:
    raise SystemExit("No token found, check .env file.")

BASE = "https://events.vex.com/api/v2"
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Accept": "application/json"}
SKU = "RE-V5RC-26-5014"

response = requests.get(f"{BASE}/events", headers = HEADERS, params = {"sku[]": SKU})
print ("Status:", response.status_code)

if (response.status_code != 200):
    print(response.text)
    raise SystemExit("Request Failed")

data = response.json()
os.makedirs("data", exist_ok = True)
with open("data/event.json","w") as f:
    json.dump(data, f, indent = 2)

print ("Saved event data to data/events.json")