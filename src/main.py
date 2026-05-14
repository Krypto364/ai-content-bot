# src/main.py

from youtube_trend_finder import get_trending_ai_topics
from script_generator import generate_script
from image_fetcher import fetch_image
from video_generator import create_video
from uploader import upload_video

import os

def run_bot():
    print("🚀 AI CONTENT BOT STARTED")

    os.makedirs("assets/output", exist_ok=True)
    os.makedirs("assets/temp", exist_ok=True)

    topics = get_trending_ai_topics()

    if not topics:
        topics = ["Top AI tools", "Best AI websites"]

    for i, topic in enumerate(topics[:2]):
        print(f"\n📊 Topic {i+1}: {topic}")

        try:
            script = generate_script(topic)
            print("✅ Script generated")

            image_path = fetch_image("AI technology", f"img_{i}")
            print("✅ Image fetched")

            output_path = f"assets/output/video_{i}.mp4"

            create_video(script, image_path, output_path)
            print("✅ Video created")

            upload_video(output_path, topic)

        except Exception as e:
            print(f"❌ Error: {e}")

    print("\n🎉 BOT RUN COMPLETED")

if __name__ == "__main__":
    run_bot()
