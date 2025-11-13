import json
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
ai_token = os.getenv("AI_TOKEN")

def process_info(bibite_data: dict, instructions: str) -> dict:
    client = genai.Client(api_key=ai_token)

    """
    Genera un Bibite a partir del prompt recibido.
    """

    prompt = f"""
    Aquí tienes un JSON que define un bibite:

    {bibite_data}

    Por favor modifícalo para que cumpla con esta descripción:
    "{instructions}".

    IMPORTANTE: responde únicamente con el JSON, sin explicaciones.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )


    print(response.text)
    return response.text
