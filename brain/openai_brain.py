import os
from google import genai

# Initialize the modern Gemini client.
# The SDK automatically handles loading the GEMINI_API_KEY from your Render Environment variables.
try:
    client = genai.Client()
except Exception as e:
    print(f"Error starting the Gemini SDK Client: {e}")
    client = None

def ask_ai(user_input: str) -> str:
    """
    Acts as NovaCore's default fallback neural brain via Gemini.
    Called automatically when no hardcoded keywords match.
    """
    if not client:
        return "System Error: The AI backend client is not configured properly."

    try:
        # Utilizing the lightning-fast flagship flash model
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_input.strip(),
        )
        
        if response and response.text:
            return response.text
        return "I processed the query but received an empty text block back."
        
    except Exception as err:
        # This streams the exact API error details straight into your Render live web dashboard logs
        print(f"[Gemini Fallback SDK Error]: {err}")
        return "Sorry, I hit a slight connection glitch while thinking."
