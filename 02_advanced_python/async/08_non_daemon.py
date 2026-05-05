import threading
import time

def monitor_tea_temp():
  while True:
    print(f"Monitoring tea temperatre....")
    time.sleep(3)

t = threading.Thread(target=monitor_tea_temp)
t.start()

print("Main program done ✅")
