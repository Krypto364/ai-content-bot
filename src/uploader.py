# src/uploader.py

import os
import json
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials

def upload_video(file_path, title):

    print("📤 Starting YouTube Upload...")

    creds_json = os.getenv("YOUTUBE_CREDENTIALS")

    if not creds_json:
        print("❌ No YouTube credentials found")
        return

    try:
        creds_dict = json.loads(creds_json)

        creds = Credentials(
            token=creds_dict.get("access_token"),
            refresh_token=creds_dict.get("refresh_token"),
            token_uri="https://oauth2.googleapis.com/token",
            client_id=creds_dict.get("client_id"),
            client_secret=creds_dict.get("client_secret")
        )

        youtube = build("youtube", "v3", credentials=creds)

        request = youtube.videos().insert(
            part="snippet,status",
            body={
                "snippet": {
                    "title": f"🔥 {title} | AI Tools 2026",
                    "description": "🚀 Discover trending AI tools & tech updates!\n\n#AI #Tech #Shorts",
                    "tags": ["AI", "Tools", "Tech", "Shorts"],
                    "categoryId": "28"
                },
                "status": {
                    "privacyStatus": "public"
                }
            },
            media_body=MediaFileUpload(file_path, chunksize=-1, resumable=True)
        )

        response = request.execute()

        print("✅ Uploaded Successfully:", response["id"])

    except Exception as e:
        print("❌ Upload failed:", str(e))
