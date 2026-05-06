def block_ip(ip):
    blocked_file = "data/blocked_ips.txt"

    # read existing blocked IPs
    try:
        with open(blocked_file, "r") as f:
            blocked_ips = f.read().splitlines()
    except FileNotFoundError:
        blocked_ips = []

    if ip in blocked_ips:
        print(f"⚠️ IP {ip} is already blocked")
        return

    print(f"🚫 Blocking IP: {ip}")

    with open(blocked_file, "a") as f:
        f.write(ip + "\n")