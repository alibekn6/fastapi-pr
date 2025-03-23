import dis

def f():
    f = open('file.txt', 'r')
    data = f.read()

# dis.dis(f)


a = 50000
b = 50000
if a is b:
    print("YEs")
else:
    print("NO") 