import _thread
import time

def print_time(threadName, delay):
    count = 0
    print("--- Thread Name = {0}".format(threadName))
    while count<5:
        time.sleep(delay)
        count = count+1
        print("{0}: {1}".format(threadName, time.ctime(time.time())))

try:
    _thread.start_new_thread(print_time,("Thread-1",2,))
    _thread.start_new_thread(print_time,("Thread-2",4,))
    print("--- thread End!")
except:
    print("--- Error: 無法處理Thread!!")
while 1:
    pass