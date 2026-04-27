from functools import wraps

def require_admin(func):
  @wraps(func)
  def wrapper(user_role):
    if user_role != "admin":
        print("Access denied: Admins only")
        return None
    else:
       return func(user_role)
    
  return wrapper

@require_admin
def access_tea_inventory(role):
   print("Access granted to tea inventory")

access_tea_inventory("user")
access_tea_inventory("admin")
