def incr():
    with open("counter.txt", "rb") as f:
        data = f.read().strip()
        cur = int(data)
    
    cur += 1
    print(cur)
    
    with open("counter.txt", "wb") as f:
        f.write(str(cur).encode())

# Run twice to match the threaded version
incr()
incr()
