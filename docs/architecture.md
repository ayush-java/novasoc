# SOC + SIEM Threat Detection Architecture

## Pipeline Flow

Linux Logs → Filebeat → Logstash → Elasticsearch → Kibana
                                      ↓
                              Python Detection Engine
                                      ↓
                         Threat Intelligence + Auto Response

## Explanation

This system collects logs from a Linux machine, processes them using the ELK stack, detects malicious activity using a Python-based detection engine, enriches data using threat intelligence APIs, and automatically responds by blocking malicious IPs and generating alerts.

## Components

### Filebeat
- Collects logs from system files
- Sends logs to Logstash

### Logstash
- Parses and processes logs
- Sends structured data to Elasticsearch

### Elasticsearch
- Stores logs
- Allows fast searching and querying

### Kibana
- Visualizes logs using dashboards

### Python Detection Engine
- Detects brute force attacks
- Applies detection rules
- Calls threat intelligence APIs

### Response System
- Blocks malicious IPs
- Logs incidents
- Triggers alerts