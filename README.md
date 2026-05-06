# 🔐 SOC + SIEM + SOAR Threat Detection & Automated Response System

## 🚀 Overview

This project is a **complete end-to-end Security Operations Center (SOC)** system that integrates **SIEM (ELK Stack)** and **SOAR (automated response)** to simulate a real-world cybersecurity pipeline.

It performs:

* Real-time log collection
* Log parsing and transformation
* Threat detection (SSH brute force)
* Automated response (IP blocking)
* Incident tracking and logging

---

## 🧠 Why This Project Matters

Modern security teams rely on **SOC + SIEM + SOAR systems** to detect and respond to threats in real-time.

This project demonstrates:

* Real-world security pipeline design
* Automation of detection and response
* Hands-on experience with industry tools
* Cloud-ready cybersecurity architecture

---

## 🏗️ Architecture

![SOC Architecture](docs/architecture.png)


```
Log Source → Filebeat → Logstash → Elasticsearch → Kibana
                                       ↓
                         Python Detection Engine
                                       ↓
                          Auto Response (SOAR)
                                       ↓
                     alerts.json + blocked_ips.txt
```

---

## ⚙️ Tech Stack

| Component        | Technology Used       |
| ---------------- | --------------------- |
| Log Collection   | Filebeat              |
| Processing       | Logstash              |
| Storage          | Elasticsearch         |
| Visualization    | Kibana                |
| Detection        | Python                |
| Automation       | Python (SOAR scripts) |
| Containerization | Docker                |

---

## 🔄 System Workflow

1. Logs are generated (SSH failed login attempts)
2. Filebeat collects logs in real-time
3. Logstash parses and structures the logs
4. Elasticsearch stores and indexes data
5. Kibana visualizes logs in dashboards
6. Python detection engine analyzes logs
7. If attack detected → IP is blocked automatically
8. Incident is logged

---

## 🚨 Detection Logic

The system detects brute-force attacks using:

* Threshold-based detection
* Time window analysis
* IP-based grouping

Example:

* More than **20 failed logins**
* Within **5 minutes**
* From the same IP

---

## ⚡ Automated Response (SOAR)

When an attack is detected:

* 🚫 Attacker IP is blocked
* 📝 Incident is logged in `alerts.json`
* 📁 IP is stored in `blocked_ips.txt`

---

## 🧪 Demo (How to Run)

### 1. Start Detection Engine

```
python3 scripts/detect_bruteforce.py
```

### 2. Simulate Attack

```
for i in {1..30}; do
  echo "Failed password for invalid user admin from 192.168.1.250 port 22 ssh2" >> data/test.log
done
```

### 3. Expected Output

```
🚨 BRUTE FORCE DETECTED from 192.168.1.250
🚫 Blocking IP: 192.168.1.250
```

---

## 📊 Kibana Dashboard

The project includes:

* Failed login attempts over time
* Top attacking IP addresses
* Real-time monitoring

---

## 📁 Project Structure

```
soc-siem-threat-detection/
├── config/
├── data/
├── docs/
│   └── architecture.png
├── scripts/
│   ├── detect_bruteforce.py
│   ├── block_ip.py
│   └── auto_block.py
├── docker-compose.yml
└── README.md
```

---

## ☁️ Cloud Deployment

This system is designed to be deployed on:

* AWS (EC2)
* Microsoft Azure
* Any Linux-based cloud environment

It is **scalable and production-ready** for real-time monitoring systems.

---

## 🧹 Features Implemented

* ✅ ELK Stack pipeline (Filebeat → Logstash → Elasticsearch → Kibana)
* ✅ Real-time log ingestion
* ✅ Custom Python detection engine
* ✅ Automated IP blocking (SOAR)
* ✅ Incident tracking system
* ✅ Dockerized architecture
* ✅ Cloud-ready design

---

## 🎯 Learning Outcomes

* Built a full SOC system from scratch
* Implemented SIEM + SOAR integration
* Designed real-time detection pipelines
* Automated threat response
* Learned industry tools used in cybersecurity

---

## 👤 Author

**Ayush Velhal**

* Fully designed and implemented independently
* End-to-end system architecture and development

---

## ⭐ Future Improvements

* Integrate real firewall APIs (AWS Security Groups / Azure NSG)
* Add email/Slack alerts
* Use machine learning for anomaly detection
* Deploy fully on cloud with monitoring

---

## 📌 Final Note

This project represents a **real-world cybersecurity system simulation**, combining **log analysis, threat detection, and automated response**, similar to enterprise SOC environments.

<!-- test -->