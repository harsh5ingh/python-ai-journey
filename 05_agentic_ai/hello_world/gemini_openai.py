import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
  api_key=os.getenv("GEMINI_API_KEY"),
  base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
  model="gemini-2.5-flash",
  messages=[
    {"role": "system", "content": "You are an expert in Maths and only and only ans maths related questions. "},
    {"role": "user", "content": "Hey, I am Harsh Singh! Nice to meet you."}
  ]
)

print(response.choices[0].message.content)
