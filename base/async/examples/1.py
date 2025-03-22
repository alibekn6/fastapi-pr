import time
import os

def clock():
    time0 = round(time.time())
    while True:
        if (round(time.time()) - time0 % 5 == 0):
            print("5 Sec")
            time.sleep(1)