import time

def long_computation():
    print("Starting computation...")

    # Simulate a heavy calculation (sum of a large range)
    total = sum(i * i for i in range(10**8))
    

    print(f"Computation finished! Result: {total}")

long_computation()