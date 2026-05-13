# src/image_fetcher.py

import requests
from PIL import Image
from io import BytesIO

def fetch_image(query, filename):

    # Use stable image source
    url = f"https://picsum.photos/720/1280"

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Image download failed")

    try:
        img = Image.open(BytesIO(response.content)).convert("RGB")
    except:
        raise Exception("Invalid image received")

    path = f"assets/temp/{filename}.jpg"
    img.save(path, "JPEG")

    return path
