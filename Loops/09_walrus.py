#value = 13
#remainder = value % 5

#if remainder:
  #print(f"Not Divisible, remainder is {remainder}")

value = 13

if (remainder := value % 5):
  print(f"Not Divisible, remainder is {remainder}")