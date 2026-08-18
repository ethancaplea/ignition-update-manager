# scripts/check_release.py

print("Ignition Update Manager Running")

import re
import requests
import xml.etree.ElementTree as ET

SITEMAP_URL = "https://inductiveautomation.com/sitemap.xml"

response = requests.get(SITEMAP_URL, timeout=30)
response.raise_for_status()

root = ET.fromstring(response.text)

namespace = {
    "sm": "http://www.sitemaps.org/schemas/sitemap/0.9"
}

versions = []

for url in root.findall("sm:url", namespace):
    loc = url.find("sm:loc", namespace)

    if loc is None:
        continue

    match = re.search(
        r"/downloads/releasenotes/(8\\.3\\.\\d+)$",
        loc.text
    )

    if match:
        versions.append(match.group(1))

print(f"Found {len(versions)} Ignition 8.3 releases")

if not versions:
    raise Exception("No 8.3 releases found")

def version_key(v):
    return tuple(map(int, v.split(".")))

latest = max(versions, key=version_key)

print(f"Latest Ignition Version: {latest}")