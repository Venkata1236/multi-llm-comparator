from google import genai
from config.settings import GEMINI_API_KEY

# Initialize client
client = genai.Client(api_key=GEMINI_API_KEY)

def get_gemini_response(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
You are a factual AI assistant.
Answer clearly and accurately.
If unsure, say you don't know.

Question: {prompt}
"""
        )

        return response.text

    except Exception as e:
        return f"Gemini Error: {e}"