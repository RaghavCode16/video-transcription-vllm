import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are an assistant that analyzes spoken conversation segments from video calls.
For each segment, extract structured metadata.

Return ONLY valid JSON in the following format:
{
  "emotion": "<single dominant emotion>",
  "tone": "<tone of voice>",
  "pace": "<slow | normal | fast>",
  "reaction": "<question | suggestion | agreement | concern | explanation | neutral>"
}
"""


def analyze_segment(text: str):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text}
        ],
        temperature=0.2,
        max_tokens=120
    )

    content = response.choices[0].message.content
    return content
