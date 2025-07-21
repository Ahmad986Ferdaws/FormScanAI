# app/parser.py

import openai
import os

openai.api_key = os.getenv(\"OPENAI_API_KEY\")

def structure_form_data(raw_text):
    prompt = f\"\"\"You are an intelligent parser. Convert the following form content into structured JSON.
    
    Text:
    {raw_text}

    Output only JSON with fields like name, date, email, total, etc.
    \"\"\"

    response = openai.ChatCompletion.create(
        model=\"gpt-4o\",
        messages=[{\"role\": \"user\", \"content\": prompt}]
    )
    return response.choices[0].message.content.strip()

if __name__ == \"__main__\":
    sample = \"Name: John Doe\\nDate: 07/20/2025\\nTotal: $1,200\\nEmail: john@example.com\"
    print(structure_form_data(sample))
