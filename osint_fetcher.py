import requests
from database.mongo_connection import insert_data

def fetch_data():
    print("Fetching threat data...")

    # Example public API (no key required demo)
    url = "https://api.ipify.org?format=json"

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()

        threat_data = {
            "ip": data["ip"],
            "threat": "unknown",
            "source": "demo_api"
        }

        insert_data(threat_data)
        print("Data stored in MongoDB")

    else:
        print("Failed to fetch data")

if __name__ == "__main__":
    fetch_data()
