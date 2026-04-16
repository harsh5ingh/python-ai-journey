menu = [
  "Masala Chai",
  "Iced Lemon Tea",
  "Green Tea",
  "Ginger Tea",
  "Iced Peach Tea",
]

#iced_tea = [ tea for tea in menu if "Iced" in tea] # Iced related print

iced_tea = [ my_tea for my_tea in menu if len(my_tea) > 10] # 10 length
print(iced_tea)