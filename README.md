# 🛡️ Advanced Threat Intelligence Platform (TIP)
### Infotact Technical Internship — Project 1: Finance & Banking

---

## Architecture Overview

```
[OSINT Feeds]          [MongoDB]          [ELK Stack]         [Dashboard]
 AlienVault OTX  →                  →   Elasticsearch   →   Flask + Kibana
 URLhaus         →  Raw Indicators  →   (Normalized)    →   SOC Dashboard
 AbuseIPDB       →  Normalized Docs →   Kibana Visuals  →   Rollback API
 VirusTotal      →                  ↓
                               [Policy Enforcer]
                                   ↓
                              [iptables DROP rules]
```

---

## Four-Week Sprint Summary

| Week | Focus | Key Deliverable |
|------|-------|----------------|
| 1 | OSINT Ingestion | `osint_aggregator.py` — scrapes 3+ feeds, stores in MongoDB |
| 2 | Normalization + SIEM | `normalizer.py` + `siem_exporter.py` — risk scoring + ES export |
| 3 | Policy Enforcement | `policy_enforcer.py` — iptables daemon, blocks score ≥ 8 |
| 4 | Dashboard + Rollback | `dashboard.py` — Flask SOC UI + `/api/rollback` endpoint |

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3.11 |
| Database | MongoDB 6 (NoSQL) |
| SIEM | ELK Stack (Elasticsearch 8 + Kibana) |
| Policy Enforcement | Linux iptables via Python subprocess |
| Dashboard | Flask + Vanilla JS |
| Containerization | Docker + Docker Compose |

---

## Setup & Running

### 1. Clone and configure environment
```bash
git clone https://github.com/YOUR_USERNAME/threat-intelligence-platform.git
cd threat-intelligence-platform
cp config/.env.example .env
# Edit .env with your API keys
```

### 2. Start all services with Docker Compose
```bash
docker-compose up -d
```

### 3. Run each pipeline stage manually
```bash
# Week 1 — Fetch OSINT data
python week1_osint/osint_aggregator.py

# Week 2 — Normalize and push to Elasticsearch
python week2_siem/normalizer.py
python week2_siem/siem_exporter.py

# Week 3 — Start policy enforcer daemon (requires root on Linux)
sudo python week3_enforcer/policy_enforcer.py

# Week 4 — Launch SOC dashboard
python week4_dashboard/dashboard.py
# Open: http://localhost:5000/dashboard
```

---

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/dashboard` | GET | SOC analyst web dashboard |
| `/api/threats` | GET | JSON list of active indicators |
| `/api/rollback` | POST | Unblock a false-positive IP |
| `/api/audit` | GET | Firewall action audit log |
| `/api/blocked` | GET | Currently blocked IPs in iptables |
| `/health` | GET | Service health check |

### Rollback Example
```bash
curl -X POST http://localhost:5000/api/rollback \
  -H "Content-Type: application/json" \
  -d '{"ip": "1.2.3.4", "reason": "false_positive_confirmed"}'
```

---

## Security Practices

- **No hardcoded credentials** — all secrets via `.env` / GitHub Secrets
- **Immutable audit log** — every firewall action logged to MongoDB
- **Rollback mechanism** — SOC analyst can reverse any automated rule
- **Idempotent blocking** — duplicate rules are never added
- **IP validation** — only valid IPv4 addresses are blocked

---

## Compliance Notes

- **PCI-DSS**: Audit log provides immutable record of all network access changes
- All sensitive data injected via environment variables
- No real internal data exposed in repository

---

## GitHub Commit Guidelines

Following the project's mandatory evaluation protocol:

```
feat: add AlienVault OTX feed integration
feat: add URLhaus malicious URL fetcher
feat: add AbuseIPDB IP reputation feed
feat: implement risk scoring normalization engine
feat: add Elasticsearch SIEM exporter
feat: implement iptables dynamic policy enforcer
feat: add SOC dashboard with rollback API
fix: handle IPv6 addresses in policy enforcer
fix: resolve Elasticsearch date mapping conflict
docs: add architecture diagram to README
```

---

## License
MIT — For educational and internship portfolio use only.
