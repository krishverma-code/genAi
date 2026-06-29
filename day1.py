import os
from google import genai

# Automatically pulls the GEMINI_API_KEY from your environment variables
client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain what Python is in 3 simple lines"
)

print(response.text)