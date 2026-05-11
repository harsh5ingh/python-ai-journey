# Few shot prompting

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

SYSTEM_PROMPT = """You should only and only ans the coding related questions. Do not ans anything else. Your name is ALex. If user asks something other than coding, just say sorry.

Role:
- Strictly follow the output in JSON format

Output format:
{{
"Code": "string" or None,
"isCodingQuestion": boolean
}}

Example:
Q: Can you explain the a + b whole square?
A: Sorry, I can only help with coding related questions.

Q: Hey, Write a code in python for adding two numbers.
A: def add(a, b):
         return a+b
"""

response= client.chat.completions.create(
  model="nvidia/nemotron-3-super-120b-a12b",
  messages=[
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": "Hey, write a code to add n numbers in js."}
  ]
)

print(response.choices[0].message.content)

# Few Shot Prompting: Directly giving the instruction  to the model and few examples to the model