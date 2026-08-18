# scripts/check_release.py

print("Ignition Update Manager Running")

import requests

url = "https://inductiveautomation.com/downloads/releasenotes"

response = requests.get(url, timeout=30)

print("Status:", response.status_code)

print("\n----- FIRST 2000 CHARACTERS -----\n")
print(response.text[:2000])
print("\n----- END -----\n")