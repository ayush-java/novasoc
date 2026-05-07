## ✅ SOAR Automation

Automated response engine built with Python.

When threats are detected:

- Malicious IPs are blocked
- Incidents are logged
- Alerts are generated
- Threat telemetry is updated

---

## ✅ Enterprise Streamlit Dashboard

Custom-built enterprise cybersecurity dashboard using:

- Streamlit
- Plotly
- Python

Dashboard includes:

- Real-time SOC metrics
- Live incident feeds
- Global cyber threat map
- MITRE ATT&CK analytics
- Severity distribution
- Threat intelligence panels
- Infrastructure monitoring
- Attack type analytics
- Cloud deployment status

---

## 🌍 Global Threat Intelligence Map

The dashboard visualizes simulated cyberattacks originating from multiple countries worldwide including:

- Russia
- China
- Iran
- North Korea
- Brazil
- Germany
- USA

---

## ⚡ Live Attack Simulation

A custom Python telemetry generator continuously creates:

- fake cyberattacks
- simulated threat activity
- real-time incident updates

This allows:

- live dashboard updates
- dynamic analytics
- realistic SOC demonstrations

---

## 🏗️ Architecture

![SOC Architecture](docs/architecture.png)

```text
Attacker Activity
        ↓
Linux Authentication Logs
        ↓
Filebeat
        ↓
Logstash
        ↓
Elasticsearch
        ↓
Python Detection Engine
        ↓
SOAR Automation
        ↓
IP Blocking + Incident Logging
        ↓
Streamlit Enterprise Dashboard
```

---

## ⚙️ Technology Stack

| Category | Technology |
|---|---|
| Frontend | Streamlit |
| Visualization | Plotly |
| Backend | Python |
| SIEM | ELK Stack |
| Cloud | AWS EC2 |
| Containers | Docker |
| Detection Engine | Python |
| Automation | Python SOAR Scripts |
| Threat Analytics | MITRE ATT&CK |
| Data Processing | Pandas |

---

## ☁️ Cloud Deployment

The platform is deployed on:

- AWS EC2 Ubuntu Server
- Dockerized infrastructure
- Public cloud-hosted dashboard

Deployment includes:

- Real-time monitoring
- SOAR automation
- Threat analytics
- Cloud infrastructure management

---

## 📊 Dashboard Features

### Overview Tab

- Total alerts
- Threat scores
- Severity charts
- Attack timelines
- Global threat map

### Incidents Tab

- Incident tables
- Live attack telemetry
- Blocked IP tracking

### Threat Intelligence Tab

- MITRE ATT&CK analytics
- Critical threat monitoring
- Threat intelligence panels

### Infrastructure Tab

- AWS infrastructure status
- Docker container monitoring
- SOC pipeline visualization

---

## 🚨 Detection Logic

The platform uses:

- threshold-based detection
- IP grouping
- time-window analysis
- threat scoring
- severity classification

Example:

- 20+ failed logins
- within 5 minutes
- from the same IP

→ triggers automated SOAR response

---

## ⚡ Automated SOAR Response

When threats are detected:

- 🚫 attacker IPs are blocked
- 📝 incidents are logged
- 📊 dashboard updates automatically
- 🌍 threat map updates in real time

---

## 📁 Project Structure

```text
soc-siem-threat-detection/
├── config/
├── data/
│   ├── alerts.json
│   └── blocked_ips.txt
├── docs/
│   └── architecture.png
├── scripts/
│   ├── detect_bruteforce.py
│   ├── block_ip.py
│   └── auto_block.py
├── dashboard.py
├── live_attack_generator.py
├── docker-compose.yml
└── README.md
```

---

## 🧪 How To Run

### 1. Clone Repository

```bash
git clone https://github.com/ayush-java/soc-siem-threat-detection.git
cd soc-siem-threat-detection
```

### 2. Create Virtual Environment

```bash
sudo apt install python3.14-venv -y
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install streamlit pandas plotly
```

### 4. Start Streamlit Dashboard

```bash
python3 -m streamlit run dashboard.py --server.port 8501 --server.address 0.0.0.0
```

### 5. Start Live Attack Generator

Open another terminal:

```bash
source venv/bin/activate
python3 live_attack_generator.py
```

---

## 🎯 Learning Outcomes

This project demonstrates:

- SOC engineering
- SIEM architecture
- SOAR automation
- Cloud deployment
- Threat intelligence
- MITRE ATT&CK analysis
- Docker containerization
- Security analytics
- Cybersecurity dashboard engineering
- Real-time monitoring systems

---

## 📌 Future Improvements

Planned upgrades:

- Machine learning anomaly detection
- Email & Slack alerting
- Firewall API integration
- Multi-cloud deployment
- Threat intelligence API integration
- Real attack telemetry ingestion
- User authentication
- Role-based SOC access control

---

## 👤 Author

**Ayush Velhal**

- Designed and implemented independently
- End-to-end architecture and development
- Cloud deployment and dashboard engineering

---

## ⭐ Final Note

This project simulates a real-world:

- Security Operations Center (SOC)
- Security Information and Event Management (SIEM)
- Security Orchestration Automation and Response (SOAR)

platform using cloud infrastructure, real-time analytics, automated response pipelines, and enterprise-style cybersecurity dashboards.