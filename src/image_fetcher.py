# src/image_fetcher.py

import requests

def fetch_image(query, filename):

    url = "https://picsum.photos/720/1280"

    path = f"assets/temp/{filename}.jpg"

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Image download failed")

    with open(path, "wb") as f:
        f.write(response.content)

    return path
