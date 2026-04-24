class Chai:
  temperature = "hot"
  strength = "strong"

cutting = Chai()
print(cutting.temperature)

cutting.temperature = "Mild"
cutting.cup = "small"
print("After changing ", cutting.temperature)
print("cup size is ", cutting.cup)
print("Direct look into the class ", Chai.temperature)

del cutting.temperature         #del -> deleting
del cutting.cup
print(cutting.temperature)
# print(cutting.cup) -> it will cause error in run