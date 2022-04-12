import queue
import threading
import time

# Main example:
# Ref: https://www.runoob.com/python3/python3-multithreading.html

# Other example:
# Ref: https://medium.com/@m7807031/python-threading-example-%E5%A4%9A%E7%B7%9A%E7%A8%8B%E7%AF%84%E4%BE%8B-50e52fc4a4d0

exitFlag = 0
class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print ("开启线程：" + self.name)
        process_data(self.name, self.q)
        print ("退出线程：" + self.name)

def process_data(threadName, q):
    while not exitFlag: # 讓所有的thread會一直循環，直到workQurey的1～5都運作結束了，exitFlag會設定為1來退出所有線程!!
        queueLock.acquire()
        if not workQueue.empty(): #讓所有運作中的線程，判斷qurey內有東西就直接運作！
            data = q.get()
            queueLock.release()
            print ("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
            print("The Thread Name:{0} is release".format(threadName))
        time.sleep(1)
        print("The Thread Name:{0} is over sleep!".format(threadName))

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# 创建新线程
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    print("The Thread Name:{0} is append".format(tName))
    threads.append(thread)
    threadID += 1

# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print ("退出主线程")