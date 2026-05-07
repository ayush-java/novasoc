import json
import random
import time
from datetime import datetime

ALERTS_FILE = "data/alerts.json"

countries = [
    "Russia",
    "China",
    "Iran",
    "North Korea",
    "USA",
    "Germany",
    "Brazil"
]

attack_types = [
    "SSH Brute Force",
    "SQL Injection",
    "DDoS Attempt",
    "Malware Activity",
    "Privilege Escalation",
    "Port Scan",
    "Suspicious Login"
]

severities = [
    "LOW",
    "MEDIUM",
    "HIGH",
    "CRITICAL"
]

mitre_tactics = [
    "Credential Access",
    "Execution",
    "Persistence",
    "Privilege Escalation",
    "Reconnaissance",
    "Impact",
    "Initial Access"
]

statuses = [
    "Blocked",
    "Monitoring",
    "Investigating"
]

def generate_ip():
    return ".".join(
        str(random.randint(1, 255))
        for _ in range(4)
    )

print("🚀 Live Attack Generator Started...")

while True:

    attack = {
        "timestamp": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "ip": generate_ip(),
        "country": random.choice(countries),
        "attack_type": random.choice(attack_types),
        "severity": random.choice(severities),
        "status": random.choice(statuses),
        "threat_score": random.randint(40, 100),
        "mitre_tactic": random.choice(mitre_tactics)
    }

    with open(ALERTS_FILE, "a") as f:
        f.write(json.dumps(attack) + "\n")

    print(
        f"🚨 New Attack Generated: "
        f"{attack['attack_type']} "
        f"from {attack['country']}"
    )

    time.sleep(5)
