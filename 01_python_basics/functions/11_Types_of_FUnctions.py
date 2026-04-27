def pure_chai(cups):
  return cups * 10

total_chai = 0

# never recommended
def impure_Chai(cups):
  global total_chai
  total_chai += cups


def pour_chai(n):
    print(n)
    if n == 0:
      return "All cups poured"
    return pour_chai(n-1)
  
print(pour_chai(3))


chai_types = ["Light", "Kadak", "Ginger", "Kadak"]

strong_chai = list(filter(lambda chai: chai != "Kadak", chai_types))

print(strong_chai)