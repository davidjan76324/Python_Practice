import threading
import time


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("{0}: {1}".format(threadName, time.ctime(time.time())))
        counter -= 1


thread1 = threading.Thread(target= print_time, args= ("Thread-1", 1, 5))
thread2 = threading.Thread(target = print_time, args=("Thread-2", 2, 5))

thread1.start()
thread2.start()
thread1.join() # 等待子執行緒結束
thread2.join()
print("End!!")
