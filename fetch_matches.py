import os, json, requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ.get("VEX_TOKEN")
if TOKEN is None:
    raise SystemExit("No token found, check .env file.")

BASE = "https://events.vex.com/api/v2"
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Accept": "application/json"}
EVENT_ID = 63046
DIVISION_ID = 1

response = requests.get(f"{BASE}/events/{EVENT_ID}/divisions/{DIVISION_ID}/matches", params = {"per_page": 250}, headers = HEADERS)
print ("Status:", response.status_code)

if (response.status_code != 200):
    print(response.text)
    raise SystemExit("Request Failed")

data = response.json()
os.makedirs("data", exist_ok = True)
with open("data/matches.json","w") as f:
    json.dump(data, f, indent = 2)

print ("Saved match data to data/matches.json")
