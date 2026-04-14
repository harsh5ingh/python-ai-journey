# def make_chai():
  #return "Here is your masala chai"
  # print("Here is your masala chai")

# return_value = make_chai()

# print(return_value)

def idle_chaiwala():
  pass

print(idle_chaiwala())

def sold_cups():
  return 120

total = sold_cups()
print(total)

def chai_status(cups_left):
  if cups_left == 0:
    return "Sorry, chai over"
  return "Chai is ready"

print(chai_status(0))
print(chai_status(5))