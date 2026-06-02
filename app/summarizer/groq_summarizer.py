import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def summarize_article(title, content):

    prompt = f"""
    Article Title:
    {title}

    Article Content:
    {content[:4000]}

    TASK:
    1. Generate a professional 3-line summary
    2. Generate one engaging discussion question
    3. Mention the main topic category
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content