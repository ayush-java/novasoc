# Detection Rules

## Rule 1: SSH Brute Force Attack

Condition:
- More than 10 failed login attempts
- From the same IP
- Within 60 seconds

Action:
- Flag IP as malicious
- Send to response system

## Rule 2: Suspicious Login Behavior

Condition:
- High number of login attempts in short time
- Repeated failed logins across accounts

Action:
- Mark as suspicious activity

## Threat Intelligence

- Check IP using external APIs (AbuseIPDB, VirusTotal)
- If IP is known malicious:
  - Increase severity
  - Trigger stronger response