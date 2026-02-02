import requests
import sys

# Target URL user se milega
url = sys.argv[1] 
print(f"[*] Starting XSS Scan on: {url}")

# HowToHunt se liye hue payloads load karo
with open('payloads.txt', 'r') as f:
    payloads = f.readlines()

for payload in payloads:
    payload = payload.strip()
    # Maan lo URL hai http://test.com?q=
    # Hum q= ke baad payload jod denge
    target_url = f"{url}{payload}"
    
    try:
        response = requests.get(target_url)
        # Agar payload wapas page par dikh gaya, matlab XSS ho sakta hai
        if payload in response.text:
            print(f"[+] VULNERABLE FOUND! Payload: {payload}")
            print(f"    Link: {target_url}")
    except:
        pass

print("[*] Scan Complete.")