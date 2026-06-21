from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

api_key=os.getenv("GEMINI_API_KEY")

client=genai.Client(api_key=api_key)
print("API Key Loaded:", api_key is not None)


while True: 
    question= input("\n You: ")

    if question.lower()== "exit":
        print("Goodbye!")
        break

    response= client.models.generate_content(
    model="gemini-2.5-flash",
    contents=question
    )
    print("\n AI Response: \n")
    print(response.text)