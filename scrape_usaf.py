import requests
from xml.etree import ElementTree as ET
from dotenv import load_dotenv
import os

load_dotenv()

def fetch_usaf_rss(url):
    url = url.strip()
    print("Fetching USAF news from RSS feed...")
    res = requests.get(url)
    print(f"Status code: {res.status_code}")

    if res.status_code != 200:
        print("Failed to fetch RSS feed.")
        return []

    root = ET.fromstring(res.content)

    items = root.findall("./channel/item")
    print(f"Found {len(items)} items.")

    headlines = []
    for item in items[:5]:
        title = item.find("title").text
        link = item.find("link").text
        headlines.append((title, link))

    return headlines

if __name__ == "__main__":
    url = os.getenv("AIR_FORCE_TIMES_RSS")
    for title, link in fetch_usaf_rss(url):
        print(f"{title}\n{link}\n")

if __name__ == "__main__":
    url = os.getenv("AF_MIL_RSS")
    for title, link in fetch_usaf_rss(url):
        print(f"{title}\n{link}\n")
