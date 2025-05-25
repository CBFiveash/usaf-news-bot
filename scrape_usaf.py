import requests
from xml.etree import ElementTree as ET

def fetch_usaf_rss(url):
    try:
        res = requests.get(url, timeout=10)
        if res.status_code != 200:
            print(f"Failed to fetch RSS feed: {res.status_code}")
            return []

        root = ET.fromstring(res.content)
        items = root.findall("./channel/item")

        headlines = []
        for item in items[:5]:
            title = item.find("title").text
            link = item.find("link").text
            headlines.append((title, link))

        return headlines

    except Exception as e:
        print(f"Error fetching RSS feed: {e}")
        return []
