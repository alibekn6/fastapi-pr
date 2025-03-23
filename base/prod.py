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



incr()
incr()

# thread

# Benchmark Results:
# Total runs: 1000
# Total time: 20.0 seconds
# Average time per run: .020000 seconds
# Runs per second: 50.00






# thread1 = threading.Thread(target=incr)
# thread2 = threading.Thread(target=incr)

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()

