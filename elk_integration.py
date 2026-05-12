from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

sample_data = { "ip": "192.168.1.100", "threat": "malware", "risk_score": 95 }

es.index(index="threat_logs", document=sample_data)

print("Data inserted into Elasticsearch")
