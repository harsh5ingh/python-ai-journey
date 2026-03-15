flavours = ["Ginger", "Out of Stock", "Lemon", "Discontinued", "Tulsi"]

for flavour in flavours:
  if flavour == "Out of Stocks":
    continue
  if flavour == "Discontinued":
    break
  #print("Discontinued item found")
    print(f"{flavour} item found")
    break
  print(f"{flavour} item found")
print(f"Out side of loop")