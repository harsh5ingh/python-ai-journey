# Prompt Styles

## Alpaca Prompt

### Instructions: <SYSTEM_PROMPT>\n

### INPUT: <USER_QUERY>

### Response: \n

# ChatML:  
{"role": "system" | "assistant" | "user", "content": "string"
}
openAI and Anthropic use this format for their chat models. The system prompt is used to set the behavior of the assistant, the user query is the input from the user, and the assistant's response is generated based on the system prompt and user query.

# INST Prompting
[INST] What is the time now? [/INST]
