from database.mongo_connection import get_all_data, insert_data

def clean_data():
    print("Cleaning data...")

    data = get_all_data()
    cleaned = []

    seen_ips = set()

    for item in data:
        ip = item.get("ip")

        if ip not in seen_ips:
            seen_ips.add(ip)
            cleaned.append(item)

    print(f"Cleaned {len(cleaned)} records")

if __name__ == "__main__":
    clean_data()