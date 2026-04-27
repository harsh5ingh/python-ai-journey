def serve_chai():
  chai_type = "Masala" # local scope
  print(f"Inside function {chai_type}")


chai_type = "Lemon"
serve_chai()
print(f"Outside function: {chai_type}")


def chai_counter():
  chai_order = "Lemon" # Enclosing Scope

  def print_order():
    chai_order = "Ginger"
    print("Inner: ", chai_order)
  print_order()
  print("Order: ", chai_order)

chai_order = "Tulsi" # Global Scope
chai_counter()
print("Global: ", chai_order)