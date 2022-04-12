import threading
import time

# 使用 threading 模块创建线程
"""
我们可以通过直接从 threading.Thread 继承创建一个新的子类，并实例化后调用 start() 方法启动新线程，即它调用了线程的 run() 方法：
"""

class myThread(threading.Thread):
    def __init__(self, threadId, name, counter):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程：" + self.name)
        #threadLock.acquire()  # 获取锁，用于线程同步
        print_time(self.name, self.counter, 5)
        print("退出线程：" + self.name)
        #threadLock.release()  # 释放锁，开启下一个线程


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("{0}: {1}".format(threadName, time.ctime(time.time())))
        counter -= 1


#对于那些需要每次只允许一个线程操作的数据，可以将其操作放到 acquire 和 release 方法之间。
#多线程的优势在于可以同时运行多个任务（至少感觉起来是这样）。但是当线程需要共享数据时，可能存在数据不同步的问题。
#threadLock = threading.Lock()


#創建新的thread
thread1 = myThread(1,"Thread-1", 1)
thread2 = myThread(2,"Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()
thread1.join() #thread 线程调用了 join() 方法，并且没有指定具体的 timeout 参数值。这意味着如果程序想继续往下执行，必须先执行完 thread 线程。
thread2.join()
print ("退出主线程")