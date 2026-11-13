import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)

languages = {
    "Hindi": "Translate the given sentence into Hindi.",
    "Telugu": "Translate the given sentence into Telugu.",
    "French": "Translate the given sentence into French.",
}


def language_translator(question, language):
    system_instruction = languages[language]
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=question,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            temperature=0.3,
            max_output_tokens=2000,
        ),
    )
    return response.text


if __name__ == "__main__":
    sentence = "Hello, how are you?"
    target_language = "Hindi"
    print(language_translator(sentence, target_language))