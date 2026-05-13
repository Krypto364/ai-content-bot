from openai import OpenAI
from config import NVIDIA_API_KEY, BASE_URL

client = OpenAI(
    api_key=NVIDIA_API_KEY,
    base_url=BASE_URL
)

def generate_script(topic):

    prompt = f"""
    Create a viral YouTube Shorts script about: {topic}

    Include:
    - Strong hook in first line
    - Fast pacing
    - Short sentences
    - Curiosity gap

    Keep under 25 seconds.
    """

    response = client.chat.completions.create(
        model="meta/llama-3.1-70b-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8,
        max_tokens=200
    )

    return response.choices[0].message.content
