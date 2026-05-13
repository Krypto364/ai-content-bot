import requests

def fetch_image(query, filename):
    url = f"https://source.unsplash.com/720x1280/?{query}"
    img_data = requests.get(url).content

    path = f"assets/temp/{filename}.jpg"
    with open(path, "wb") as f:
        f.write(img_data)

    return path
