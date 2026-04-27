def brew_Chai(flavor):
  if flavor not in ["masala", "ginger", "elaichi"]:
       raise ValueError("Unsupported chai flavor...")
  print(f"brewing {flavor} chai...")


brew_Chai("mint")
#ValueError: Unsupported chai flavor...