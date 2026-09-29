import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing from .env")

client = genai.Client(api_key=api_key)

question = input("Ask Gemini: ")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=question
)

print("\nGemini:")
print(response.text)