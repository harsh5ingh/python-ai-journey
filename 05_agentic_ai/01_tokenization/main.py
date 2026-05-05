import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey There! My name is Harsh Singh"
tokens = enc.encode(text)

# Tokens [25216, 3274, 0, 3673, 1308, 382, 7591, 1116, 44807]
print("Tokens", tokens)

decoded = enc.decode([25216, 3274, 0, 3673, 1308, 382, 7591, 1116, 44807])

print("Decoded", decoded)