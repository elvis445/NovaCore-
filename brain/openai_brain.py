import os
from google import genai

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def ask_ai(user):
    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=user
        )

        return response.text

    except Exception as e:
        return "AI error: " + str(e)
