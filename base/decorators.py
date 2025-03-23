
def display(func):
    def inner():
        print("The current user is ", end="")
        return func()
    return inner


def hello(func):
    def inner():
        print("Hello my name is ", end="")
        return func()
    return inner


@display
def who():
    print("Alibek")

@hello
def whoo():
    print("Arurur")

who()
whoo()





def pretty_sum(func):
    def inner(a, b):
        print(str(a) + " + " + str(b) + " is", end=" ")
        func(a,b)
    return inner

@pretty_sum
def add(a,b) -> int:
    sum = a + b
    print(sum)

add(4,3)





import time


def measure_time(func):                                                                                                                                                                                                    
    def inner(*arg):                                                                                                      
        t = time.time()
        res = func(*arg)
        print("Function took " + str(time.time()-t) + " seconds to run " + str(res))                                                    
        return res
    return inner
                         

@measure_time
def func(n):
    time.sleep(n)


func(5)

                                                                                 
                 
@measure_time
def som(a, b):
    return a+b

som(131341341231, 92934124313)