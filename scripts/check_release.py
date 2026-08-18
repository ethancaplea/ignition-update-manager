# scripts/check_release.py

print("Ignition Update Manager Running")

import requests

urls = [
    "https://inductiveautomation.com/downloads/releasenotes",
    "https://inductiveautomation.com/sitemap.xml",
    "https://inductiveautomation.com/robots.txt"
]

for url in urls:
    try:
        r = requests.get(url, timeout=30)

        print("=" * 60)
        print(url)
        print("Status:", r.status_code)
        print(r.text[:500])
        print()
    except Exception as e:
        print(url, e)