class OutOfIngredientsError(Exception):
  pass

def make_Chai(milk, sugar):
  if milk == 0 or sugar == 0:
    raise OutOfIngredientsError("Missing milk or sugar")
  print("Chai is ready...")

make_Chai(0, 1)
#custom error