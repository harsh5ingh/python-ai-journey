from multiprocessing import Process
import time

def cpu_heavy():
  print(f"Crunching some numbers....")
  total = 0
  for i in range(10**8):
    total += i
  print("DONE ✅")

if __name__ == "__main__":
  start = time.time()
  Processes = [Process(target=cpu_heavy) for _ in range(2)]
  [t.start() for t in Processes]
  [t.join() for t in Processes]

  print(f"Time taken: {time.time() - start:.2f} seconds")