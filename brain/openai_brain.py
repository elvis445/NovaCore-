import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def ask_ai(user):
    response = client.responses.create(
        model="gpt-5.6-luna",
        input=user
    )

    return response.output_text
