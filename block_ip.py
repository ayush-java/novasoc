import os
import sys

def block_ip(ip):
    print(f"[+] Blocking IP: {ip}")
    os.system(f"echo 'Blocked {ip}' >> blocked_ips.txt")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        ip = sys.argv[1]
        block_ip(ip)
    else:
        print("No IP provided")