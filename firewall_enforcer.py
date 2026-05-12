import subprocess from mongodb_connection import collection

records = collection.find({"risk_score": {"$gt": 80}})

for record in records: ip = record["ip"]
command = [
    "sudo",
    "iptables",
    "-A",
    "INPUT",
    "-s",
    ip,
    "-j",
    "DROP"
]

subprocess.run(command)
print(f"Blocked IP: {ip}")
