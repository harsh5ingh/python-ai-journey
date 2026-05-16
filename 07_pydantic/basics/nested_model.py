from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
  street: str
  city: str
  postal_code: str

class User(BaseModel):
  id: int
  name: str
  address: Address

address = Address(
  street="123 something",
  city= "Patna",
  postal_code="800001",
)

user = User(
  id=1,
  name="Harsh",
  address=address,
)

user_data = {
  "id": 1,
  "name": "Harsh",
  "address": {
    "street": "321 something",
    "city": "Bikram",
    "postal_code": "801104",
  }
}

user= User(**user_data)
print(user)
