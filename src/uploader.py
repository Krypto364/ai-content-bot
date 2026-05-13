# src/uploader.py

import os
import json
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials

def upload_video(file_path, title):

    print("📤 Starting YouTube Upload...")

    # Load credentials
    creds = Credentials.from_authorized_user_info(
        json.loads(os.getenv("YOUTUBE_CLIENT_SECRET"))
    )

    youtube = build("youtube", "v3", credentials=creds)

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": "🔥 AI Tools & Tech Updates Daily",
                "tags": ["AI", "Tech", "Tools", "Shorts"],
                "categoryId": "28"
            },
            "status": {
                "privacyStatus": "public"
            }
        },
        media_body=MediaFileUpload(file_path)
    )

    response = request.execute()

    print("✅ Uploaded to YouTube:", response["id"])
