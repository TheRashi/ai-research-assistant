from dotenv import load_dotenv
import os
from google import genai
from prompts import (
    DSA_MENTOR,
    CAREER_COACH,
    GENAI_MENTOR
)

load_dotenv()

api_key=os.getenv("GEMINI_API_KEY")

client=genai.Client(api_key=api_key)

print("\n Choose Persona")
print("1. DSA Mentor")
print("2. Career Coach")
print("3. GENAI Mentor")
choice=int(input("Enter choice (1-3): "))

if choice==1:
    selected_prompt=DSA_MENTOR
elif choice==2:
    selected_prompt=CAREER_COACH
elif choice==3:
    selected_prompt=GENAI_MENTOR
else:
    print("Invalid choice. Defaulting to genai mentor.")
    selected_prompt=GENAI_MENTOR


while True: 
    question= input("\n You: ")

    if question.lower()== "exit":
        print("Goodbye!")
        break

    prompt = f"""
    {selected_prompt}

    User Question:
    {question}
    """
    try:
        response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
        )
        print("\n AI Response: \n")
        print(response.text)

    except Exception as e:
        print(f"An error occured: {e}")