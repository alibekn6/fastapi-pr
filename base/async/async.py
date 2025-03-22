from threading import Thread
import time

results = []

def background_task():
    print("Starting computation...")

    # Simulate a heavy calculation (sum of a large range)
    total = sum(i * i for i in range(10**8))
    results.append(total)
    

    return total


# we need final result from background_task
def main():
    t = Thread(target=background_task)
    t.start()
    t.join()
    print(f"Main thread finished and result")
    print(f"Empty right now" if not results else "Not empty")


main()

# if you dont rely on background_task results you dont need join()