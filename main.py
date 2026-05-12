import random
from trend_finder import get_trending_topics
from ai_tool_finder import get_ai_tools
from script_generator import generate_script
from video_generator import create_video
from uploader import upload_video

def run_bot():
    mode = random.choice(["viral", "transform"])

    if mode == "viral":
        print("🔥 Running Viral Mode")

        topics = get_trending_topics()
        for i, topic in enumerate(topics):
            text = f"Trending: {topic}"
            output = f"assets/output/viral_{i}.mp4"

            create_video(text, output)
            upload_video(output, text)

    else:
        print("🤖 Running Transform Mode")

        tools = get_ai_tools()
        for i, tool in enumerate(tools[:2]):
            script = generate_script(tool["name"])
            output = f"assets/output/ai_{i}.mp4"

            create_video(script, output)
            upload_video(output, tool["name"])

if __name__ == "__main__":
    run_bot()
