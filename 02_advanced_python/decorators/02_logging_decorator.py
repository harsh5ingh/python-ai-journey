from functools import wraps

def log_Activity(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    print(f"🚀 Calling: {func.__name__}")
    result = func(*args, **kwargs)
    print(f"✅ Finished: {func.__name__}")
    return result
  return wrapper

@log_Activity
def brew_Chai(type, milk="no"):
    print(f"Brewing {type}and chai")
brew_Chai("Masala")

