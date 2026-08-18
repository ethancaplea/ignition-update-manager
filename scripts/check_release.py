# scripts/check_release.py

print("Ignition Update Manager Running")

import requests

url = "https://inductiveautomation.com/downloads/releasenotes"

response = requests.get(url, timeout=30)

print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    print("Release notes page reachable")
else:
    print("Unable to reach release notes page")