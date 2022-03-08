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
        print_time(self.name, self.counter, 5)
        print("退出线程：" + self.name)


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("{0}: {1}".format(threadName, time.ctime(time.time())))
        counter -= 1

#創建新的thread
thread1 = myThread(1,"Thread-1", 1)
thread2 = myThread(2,"Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()
thread1.join() #thread 线程调用了 join() 方法，并且没有指定具体的 timeout 参数值。这意味着如果程序想继续往下执行，必须先执行完 thread 线程。
thread2.join()
print ("退出主线程")