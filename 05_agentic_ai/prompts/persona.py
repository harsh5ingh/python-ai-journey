# Persona Based Prompting

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(ROOT_DIR))

import os

from dotenv import load_dotenv
from openai import OpenAI

import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

SYSTEM_PROMPT = """
     You are an AI Persona Assistant named Harsh Singh.
     You are acting on behalf of Harsh Singh who is 22 years old Tech enthusiastic and principle engineer. Your main tech stack is JS and Python and You are learning GenAI these days.

     Examples:
     Q: Hey
     A: Hey, Whats up!

     (100 - 150 examples)
"""

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages= [
      {"role": "system", "content": SYSTEM_PROMPT},
      {"role": "user", "content": "HWho are you?"}
    ]
  )

print("Response: ", response.choices[0].message.content)