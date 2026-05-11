# Chain of Thought Prompting

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(ROOT_DIR))

import config
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
   You're an expert AI Assistant in resolving user queries using chain of thoughts.
   You work on START, PLAN and OUTPUT steps.
   You need to first PLAN what needs to be done. The PLAN can be multiple steps.
   Once you think enough PLAN has been done, finally you can give an OUTPUT.

   Rules:
   - Strictly follow the given JSON output format
   - Only run onw step at a time.
   - The sequence of steps is START ( where user gives an input), PLAN (which is going to the displayed to the user).

   Output JSON format:
   { "step": "START" | "PLAN" | "OUTPUT", "content": "string" }

   Example:
   START: Hey, can you solve 2 + 3 * 5 / 10
   PLAN: {"step": "PLAN": "content": "Seems like user is interested in math problem" }
   PLAN: {"step": "PLAN": "content": "looking at the problem, we should solve this using BODMAS method"}
   PLAN: {"step": "PLAN": "content": "Yes, The BODMAS is correct thing to be done here"}
   PLAN: {"step": "PLAN": "content": "first we must multiply 3 * 5 which is 15"}
   PLAN: {"step": "PLAN": "content": "Now the equation is 2 + 15 / 10 "}
   PLAN: {"step": "PLAN": "content": "We must perform divide that is 15 / 10 = 1.5"}
   PLAN: {"step": "PLAN": "content": "Now the new equation is 2 + 1.5"}
   PLAN: {"step": "PLAN": "content": "Now finally lets perform the add 3.5"}
   PLAN: {"step": "PLAN": "content": "Great, we have solved and finally left with 3.5 as ans"}
   PLAN: {"step": "PLAN": "content": "3.5"}

"""

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    response_format={"type": "json_object"},
    messages=[
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": "Hey, write a code to add n numbers in js."},
    # Manually keep adding messages to History
    {"role": "assistant", "content": json.dumps({"step": "START", "content": "You want a Javascript code to add n numbers."})},
    {"role": "assistant", "content": json.dumps({"step": "PLAN", "content": "To add n numbers in Javascript, we can define a function that takes an array of numbers as input and returns their sum."})},
    {"role": "assistant", "content": json.dumps({
  "step": "PLAN", 
   "content": "We can utilize the built-in reduce method in Javascript, which applies a function against an accumulator and each element in the array (from left to right) to reduce it to a single value, such as sum."})},
   {"role": "assistant", "content": json.dumps({
  "step": "PLAN", 
   "content": "The function will look something like this: function addNumbers(arr) { return arr.reduce((a, b) => a + b, 0); }. This function will take an array of numbers, add them together, and return the result."})}

  ]
)
print(response.choices[0].message.content)