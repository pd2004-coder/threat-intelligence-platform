from mongodb_connection import collection

records = collection.find()

for record in records: if "risk_score" not in record: collection.update_one( {"_id": record["_id"]}, {"$set": {"risk_score": 50}} )

print("Normalization completed")
