import threading
import time

counter = 0

def increment():
    global counter
    for _ in range(10000000):
        # Force more context switches by adding a tiny sleep
        if _ % 1000 == 0:
            time.sleep(0.000001)  
        counter += 1

# Create two threads
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

# Start threads
thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()

print("Counter:", counter)