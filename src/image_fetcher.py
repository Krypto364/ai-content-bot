# src/image_fetcher.py

import requests
from PIL import Image
from io import BytesIO

def fetch_image(query, filename):
    url = f"https://source.unsplash.com/720x1280/?{query}"

    response = requests.get(url)

    img = Image.open(BytesIO(response.content)).convert("RGB")

    path = f"assets/temp/{filename}.jpg"
    img.save(path, "JPEG")

    return path
