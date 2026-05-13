# src/main.py

from youtube_trend_finder import get_trending_ai_topics
from script_generator import generate_script
from image_fetcher import fetch_image
from video_generator import create_video
from uploader import upload_video

import os

def run_bot():
    print("🚀 LEVEL 3 AI CONTENT BOT STARTED")

    # Step 1: Get trending topics
    topics = get_trending_ai_topics()

    if not topics:
        print("❌ No topics found, using fallback")
        topics = ["Top AI tools 2026", "Best AI websites"]

    # Step 2: Loop through topics
    for i, topic in enumerate(topics[:2]):
        print(f"\n📊 Processing Topic {i+1}: {topic}")

        try:
            # Step 3: Generate script using NVIDIA AI
            script = generate_script(topic)
            print("✅ Script generated")

            # Step 4: Fetch background image
            image_path = fetch_image("artificial intelligence technology", f"img_{i}")
            print("✅ Image fetched")

            # Step 5: Create video with voice
            output_path = f"assets/output/video_{i}.mp4"
            create_video(script, image_path, output_path)
            print("✅ Video created")

            # Step 6: Upload (currently print only)
            upload_video(output_path, topic)
            print("✅ Upload step completed")

        except Exception as e:
            print(f"❌ Error processing topic: {e}")

    print("\n🎉 BOT RUN COMPLETED")

if __name__ == "__main__":
    run_bot()
