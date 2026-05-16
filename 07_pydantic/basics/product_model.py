from pydantic import BaseModel

class Product(BaseModel):
  id: int
  name: str
  price: float
  in_stock: bool = True

product_one = Product(id=1, name="Laptop", price=999.99, in_stock=True)

product_two = Product(id=2, name="Macbook", price=799.9, in_stock=True)

product_three = Product(id=3, name= "Keyboard", price=24.9, in_stock=False)

print("First Product: ", product_one)