# 🔐 SOC + SIEM Threat Detection & Automated Response System

## 🚀 Overview

This project simulates a real-world Security Operations Center (SOC) pipeline using the ELK Stack (Elasticsearch, Logstash, Kibana).

It ingests system logs, detects SSH brute-force attacks, visualizes attack patterns, and performs automated response actions such as blocking malicious IPs.

---

## 🧠 Key Features

- 📥 Log ingestion using Filebeat
- 🔄 Log processing and parsing using Logstash
- 🗄️ Storage and indexing using Elasticsearch
- 📊 Real-time dashboards using Kibana
- 🚨 Detection of SSH brute-force attacks
- 🤖 Automated response system (IP blocking simulation)
- 📈 Visual analytics for attack trends and top attackers

---

## 🛠️ Tech Stack

- ELK Stack (Elasticsearch, Logstash, Kibana)
- Filebeat
- Docker & Docker Compose
- Python (automation scripts)

---

## 📊 Dashboard Visualizations

- **Failed Login Attempts Over Time**  
  → Detects spikes indicating brute-force attacks  

- **Top Attacking IPs**  
  → Identifies most frequent attack sources  

---

## 🧱 Architecture

```text
Filebeat → Logstash → Elasticsearch → Kibana
                      ↓
                Python Scripts
                      ↓
               Automated Response