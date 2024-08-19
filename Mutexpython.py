import threading
import time

class Mutex:
    def __init__(self):
        self.mutex = threading.Lock()
    def acquire(self):
        self.mutex.acquire()
    def release(self):
        self.mutex.release()

def task(name, delay, mutex):
    print(f"{name,} is waiting to aquire the mutex")
    mutex.acquire()
    print(f"{name,} aquired the mutex")
    print(f"{name,} started")
    time.sleep(delay)
    print(f"{name,} completed")
    mutex.release()
    print(f"{name,} released the mutex")

mutex = Mutex()

threads = []
for i, delay in zip(range(1,5), [2,1,3,1.5]):
    thread = threading.Thread(target=task, args=(f"Task {i}", delay, mutex))
    thread.start()

for thread in threads:
    thread.join()

