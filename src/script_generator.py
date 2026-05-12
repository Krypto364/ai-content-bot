from openai import OpenAI
from config import NVIDIA_API_KEY, BASE_URL

client = OpenAI(
    api_key=NVIDIA_API_KEY,
    base_url=BASE_URL
)

def generate_script(topic):
    prompt = f"""
    Create a short 20-second viral script about {topic}.
    Make it engaging, fast, and social-media style.
    """

    response = client.chat.completions.create(
        model="meta/llama-3.1-70b-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=150
    )

    return response.choices[0].message.content
