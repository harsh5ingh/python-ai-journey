def serve_chai():
  yield "Cup 1: Masala Chai"
  yield "Cup 2: Ginger Chai"
  yield "Cup 3: Elaichi Chai"

# yield keywords turns a function into a function generator

stall = serve_chai()

for cup in stall:
  print(cup)

def get_chai_list():
  return ["Cup 1", "Cup 2", "Cup 3"]


# Generator Function

def get_Chai_get():
  yield "Cup 1"
  yield "Cup 2"
  yield "Cup 3"

chai = get_Chai_get()
print(next(chai))
print(next(chai))
print(next(chai))
print(next(chai)) # gives error bcoz 3 Cups hi tha