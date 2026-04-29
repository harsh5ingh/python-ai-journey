from multiprocessing import Process, Queue

def prepare_Chai(queue):
  queue.put("Masala Chai is ready")

if __name__ == "__main__":
     queue = Queue()
     p = Process(target=prepare_Chai, args=(queue, ))
     p.start()
     p.join()
     print(queue.get())