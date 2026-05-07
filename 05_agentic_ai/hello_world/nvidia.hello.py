import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
  api_key=os.getenv("NVIDIA_API_KEY"),
  base_url="https://integrate.api.nvidia.com/v1"
)

response= client.chat.completions.create(
  model="nvidia/nemotron-3-super-120b-a12b",
  messages=[
    {"role": "system", "content": "You are an expert in Maths and only and only ans maths related questions. "},
    {"role": "user", "content": "Hey, I am Harsh Singh! Nice to meet you."}
  ]
)

print(response.choices[0].message.content)