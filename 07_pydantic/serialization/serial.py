from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
  street: str
  city: str
  postal_code: str

class User(BaseModel):
  id:int
  name: str
  email: str
  is_active: bool = True
  createdAt: datetime
  address: Address
  tags: List[str] = []

  model_config = ConfigDict(
    json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
   )

user = User(
  id=1,
  name="Harsh",
  email="h@harsh.ai",
  createdAt=datetime(2026, 5, 16, 14, 30, 20),
  address=Address(
    street="Something",
    city="Patna",
    postal_code="800001",
  ),
  is_active=False,
  tags=["premium", "subscriber"]
)

Python_dict = user.model_dump()
print(user)
print("="*30)
print(Python_dict)

json_str = user.model_dump_json()
print("="*30)
print(json_str)