class ChaiOrder:

  def __init__(self, tea_type, sweetness, size):
    self.tea_type = tea_type
    self.sweetness = sweetness
    self.size = size

  @classmethod
  def from_dict(cls, order_data):
    # this means I'm passing the whole value of line 3 to 6. 
    return cls(
      order_data["tea_type"],
      order_data["sweetness"],
      order_data["size"]
    )
  
  @classmethod
  def from_string(cls, order_string):
    tea_type, sweetness, size = order_string.split("-")
    return cls(tea_type, sweetness, size)
  
class chaiUtils:
  @staticmethod
  def is_valid_size(size):
    return size in ["small", "medium", "large"]
  
order1 = ChaiOrder.from_dict({"tea_type": "masala", "sweetness": "medium", "size": "large"})

order2 = ChaiOrder.from_string("Ginger-low-small")

order3 = ChaiOrder("large", "low", "large")
print(order1.__dict__)
print(order2.__dict__)
print(order3.__dict__)