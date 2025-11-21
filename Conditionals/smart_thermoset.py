device_status = "active"
tempurature = 38

if device_status == "active":
  if tempurature > 35:
    print("High Temperature alert!")
  else:
    print("Temperature is ")
else:
  print("Device is offline")