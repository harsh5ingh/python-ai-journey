# Zero Shot

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(ROOT_DIR))

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
  api_key=os.getenv("NVIDIA_API_KEY"),
  base_url="https://integrate.api.nvidia.com/v1"
)



SYSTEM_PROMPT = "You should only and only ans the coding related questions. Do not ans anything else. Your name is ALex. If user asks something other than coding, just say sorry"

response= client.chat.completions.create(
  model="nvidia/nemotron-3-super-120b-a12b",
  messages=[
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": "Hey, Can you write a python code to translate the word Hello to Hindi."}
  ]
)

print(response.choices[0].message.content)

#1. Zero shot prompting: Directly giving the instruction to the model