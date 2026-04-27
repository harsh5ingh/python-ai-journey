chai_type = "Ginger Chai"
customer_name = "Priya"

print(f"Order for {customer_name} : {chai_type} please !")

chai_description = "Aromatic and Bold"
print(f"First word: {chai_description[0:8]}")
print(f"Last word: {chai_description[12:8]}")
print(f"Opposite Last word: {chai_description[::-1]}")

lable_text = "Chai Spécial"
ecoded_label = lable_text.encode("utf-8")
print(f"Non Encoded Label: {lable_text}")
print(f"Encoded Label: {ecoded_label}")
decoded_label = ecoded_label.decode("utf-8")
print(f"Decoded Label: {decoded_label}")