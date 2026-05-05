import re
import subprocess

LOG_FILE = "test.log"

def extract_ips():
    ips = set()

    with open(LOG_FILE, "r") as f:
        for line in f:
            if "Failed password" in line:
                match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
                if match:
                    ips.add(match.group(1))

    return ips

def block_ips(ips):
    for ip in ips:
        print(f"[+] Sending {ip} to blocker...")
        subprocess.run(["python3", "block_ip.py", ip])

if __name__ == "__main__":
    ips = extract_ips()
    block_ips(ips)