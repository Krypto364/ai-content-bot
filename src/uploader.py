# src/uploader.py

import os
import json
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def upload_video(file_path, title):

    print("📤 Uploading to YouTube...")

    credentials_json = os.getenv("YOUTUBE_CREDENTIALS")

    if not credentials_json:
        print("❌ No YouTube credentials found")
        return

    creds_dict = json.loads(credentials_json)

    youtube = build("youtube", "v3", developerKey=creds_dict.get("api_key"))

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": "🔥 AI Tools & Tech Updates",
                "tags": ["AI", "Tools", "Tech"],
                "categoryId": "28"
            },
            "status": {
                "privacyStatus": "public"
            }
        },
        media_body=MediaFileUpload(file_path)
    )

    response = request.execute()

    print("✅ Uploaded:", response["id"])
