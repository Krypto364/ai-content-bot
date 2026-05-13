# src/youtube_trend_finder.py

import requests
from bs4 import BeautifulSoup

def get_trending_ai_topics():
    url = "https://www.youtube.com/results?search_query=ai+tools"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    topics = []

    for a in soup.find_all("a"):
        title = a.get("title")
        if title and len(title) > 20:
            topics.append(title)

    # fallback if nothing found
    if not topics:
        return ["Top AI tools 2026", "Best AI websites"]

    return topics[:2]
