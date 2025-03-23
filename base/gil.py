import threading

lock = threading.Lock()

def increment():
    with lock:

        f = open("file.txt", "r")
        data = f.read().strip()
        number = int(data)
        for _ in range(10000000):
            number += 1

        f = open("file.txt", "w")
        f.write(str(number))


thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

