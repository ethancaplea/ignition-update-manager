# scripts/check_release.py

print("Ignition Update Manager Running")

import json
import re
from pathlib import Path

import requests

BASE_DIR = Path(__file__).resolve().parent.parent
STATE_FILE = BASE_DIR / "state" / "latest_release.json"

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

state = json.loads(STATE_FILE.read_text())

saved_version = state["latestSeenVersion"]

print(f"Latest Ignition Version: {latest_version}")
print(f"Previously Seen Version: {saved_version}")

if latest_version == saved_version:
    print("NO_UPDATE")
else:
    print("NEW_UPDATE")

    state["latestSeenVersion"] = latest_version

    STATE_FILE.write_text(
        json.dumps(state, indent=4)
    )

    print(f"Saved version {latest_version}")