from threading import Thread
from datetime import datetime
import time
import datetime

gfib = 0


def my_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return my_fib(n-1) + my_fib(n-2)


def write_log():

    global gfib
    with open("serie.txt", "a") as f:
        for i in  range(10):
            i+=1
            log_string = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) +"          " + "{}".format(gfib) + "\n"
            f.write(log_string)
            time.sleep(2)


        f.close()


n=0
unThread = Thread(target=write_log, )
unThread.start()


for n in range(666):
    n += 1
    x = my_fib(n)
    print(x)
    gfib = x
    time.sleep(0.5)


