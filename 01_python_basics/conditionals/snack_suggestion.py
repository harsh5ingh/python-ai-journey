snack = input("Enter your preffered snack: ").lower()

# print(f"user said: {snack}")

if snack == "cookies" or snack == "samosa":
  print(f"Great Choice! We'll serve you {snack}.")
else:
  print("Sorry, we only serve Cookies or Samosa with Tea")