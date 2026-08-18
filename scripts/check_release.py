# scripts/check_release.py

print("Ignition Update Manager Running")

import re
import requests

url = "https://inductiveautomation.com/downloads/"

response = requests.get(url, timeout=30)
response.raise_for_status()

match = re.search(
    r"ignition\\u002D(\d+\.\d+\.\d+)\\u002Dwindows\\u002D64\\u002Dinstaller\.exe",
    response.text,
    re.IGNORECASE
)

if not match:
    raise Exception("Unable to determine latest Ignition version")

latest_version = match.group(1)

print(f"Latest Ignition Version: {latest_version}")