import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    print("Gemini API key not found. Please set it in the .env file.")
else:
    genai.configure(api_key=GEMINI_API_KEY)

    print("Available models that support 'generateContent':")
    for m in genai.list_models():
      if 'generateContent' in m.supported_generation_methods:
        print(m.name)
