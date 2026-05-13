import requests
from bs4 import BeautifulSoup

def get_trending_ai_topics():
    url = "https://www.youtube.com/results?search_query=ai+tools"
    headers = {"User-Agent": "Mozilla/5.0"}

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    titles = []

    for link in soup.find_all("a"):
        title = link.get("title")
        if title and len(title) > 20:
            titles.append(title)

    return titles[:2] if titles else ["Top AI tools", "New AI websites"]
