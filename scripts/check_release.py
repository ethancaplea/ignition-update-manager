# scripts/check_release.py

print("Ignition Update Manager Running")

import json
import re
from pathlib import Path

import requests

STATE_FILE = Path("state/latest_release.json")

url = "https://inductiveautomation.com/downloads/releasenotes"

response = requests.get(url, timeout=30)

response.raise_for_status()

matches = re.findall(r"Version\\s+(8\\.3\\.\\d+)", response.text)

if not matches:
    raise Exception("Unable to find Ignition 8.3 versions")

latest_version = matches[0]

print(f"Latest version found: {latest_version}")

state = json.loads(STATE_FILE.read_text())

previous_version = state["latestSeenVersion"]

if latest_version == previous_version:
    print("No new releases detected")
else:
    print(f"NEW RELEASE DETECTED: {latest_version}")
    print(f"Previous version: {previous_version}")