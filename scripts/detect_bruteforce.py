import time
import json
from collections import defaultdict

# ===== CONFIG =====
LOG_FILE = "data/test.log"
ALERT_FILE = "data/alerts.json"

THRESHOLD = 10        # number of attempts
TIME_WINDOW = 60      # seconds
COOLDOWN = 60         # seconds between alerts for same IP

# ===== STATE =====
attempts = defaultdict(list)
last_alert_time = {}

# ===== OPTIONAL AUTO BLOCK =====
try:
    from block_ip import block_ip
except ImportError:
    def block_ip(ip):
        print(f"⚠️ block_ip function not found, skipping block for {ip}")


# ===== HELPER FUNCTION =====
def extract_ip(line):
    parts = line.split()
    if "from" in parts:
        return parts[parts.index("from") + 1]
    return None


# ===== ALERT LOGGING =====
def log_alert(ip, count):
    alert = {
        "ip": ip,
        "attempts": count,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

    with open(ALERT_FILE, "a") as f:
        f.write(json.dumps(alert) + "\n")


# ===== MAIN DETECTION =====
def detect():
    print("🚀 Starting Brute Force Detection...\n")

    with open(LOG_FILE, "r") as f:
        f.seek(0, 2)  # move to end of file

        while True:
            line = f.readline()

            if not line:
                time.sleep(1)
                continue

            if "Failed password" in line:
                ip = extract_ip(line)
                if not ip:
                    continue

                now = time.time()
                attempts[ip].append(now)

                # keep only recent attempts
                attempts[ip] = [t for t in attempts[ip] if now - t <= TIME_WINDOW]

                if len(attempts[ip]) >= THRESHOLD:

                    # cooldown check
                    if ip not in last_alert_time or (now - last_alert_time[ip] > COOLDOWN):

                        print(f"🚨 BRUTE FORCE DETECTED from {ip} ({len(attempts[ip])} attempts)")

                        # log alert
                        log_alert(ip, len(attempts[ip]))

                        # block IP
                        block_ip(ip)

                        # update last alert time
                        last_alert_time[ip] = now

                    # reset attempts (prevents spam)
                    attempts[ip] = []


# ===== RUN =====
if __name__ == "__main__":
    detect()