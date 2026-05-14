import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(ROOT_DIR))

import os

from dotenv import load_dotenv
from openai import OpenAI
import requests

load_dotenv()

client = OpenAI(
  api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)
def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"
    
    return "Something went wrong"

def main():
    user_query = input("> ")
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages= [
            {"role": "user", "content": user_query}
    ]
  )

    print(f"🤖:  {response.choices[0].message.content}")

main()
