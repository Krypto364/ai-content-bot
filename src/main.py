# src/main.py

from script_generator import generate_script
from image_fetcher import fetch_image
from video_generator import create_video
from uploader import upload_video

import os

def run_bot():
    print("🚀 TEST MODE: ONE VIDEO")

    os.makedirs("assets/output", exist_ok=True)
    os.makedirs("assets/temp", exist_ok=True)

    topic = "Top AI tools 2026"

    try:
        script = generate_script(topic)
        print("✅ Script generated")

        image_path = fetch_image("AI technology", "test_img")
        print("✅ Image fetched")

        output_path = "assets/output/test_video.mp4"

        create_video(script, image_path, output_path)
        print("✅ Video created")

        upload_video(output_path, topic)

    except Exception as e:
        print("❌ Error:", str(e))

    print("🎉 TEST COMPLETED")

if __name__ == "__main__":
    run_bot()
