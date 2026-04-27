#value = 13
#remainder = value % 5

#if remainder:
  #print(f"Not Divisible, remainder is {remainder}")

value = 13

if (remainder := value % 5):             # Walrus ( := ) 
  print(f"Not Divisible, remainder is {remainder}")

available_sizes = ["small", "medium", "large"]

if (requested_size := input("Enter your chai cup size: ")) in available_sizes:
  print(f"Serving {requested_size} chai")
else:
  print(f"Size is unavailable = {requested_size}")


flavors = ["masala", "ginger", "lemon", "mint"]

print("Available flavors: ", flavors)

while (flavor := input("Choose your flavour: ")) not in flavors:
  print(f"Sorry, {flavor} is not available, right now")

print(f"You choose {flavor} chai")