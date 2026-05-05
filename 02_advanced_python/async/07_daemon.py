# Daemon threads are those threads that are background threads that automatically shut down when the main program exits.

import threading
import time

def monitor_tea_temp():
  while True:
    print(f"Monitoring tea temperatre....")
    time.sleep(3)

t = threading.Thread(target=monitor_tea_temp, daemon=True)
t.start()

print("Main program done ✅")
