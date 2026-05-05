import time
import subprocess

print("[+] Auto-block system started...")

while True:
    print("[+] Checking logs...")
    
    subprocess.run(["python3", "extract_and_block.py"])
    
    time.sleep(10)  # wait 10 seconds