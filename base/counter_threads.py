import threading

lock = threading.Lock()

def incr():
    with lock:
        with open("counter.txt", "rb") as f:
            data = f.read().strip()
            cur = int(data)
        
        cur += 1

        print(cur)

        with open("counter.txt", "wb") as f:
            f.write(str(cur).encode())

thread1 = threading.Thread(target=incr)
thread2 = threading.Thread(target=incr)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
