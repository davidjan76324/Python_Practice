from curses import nonl
from re import I


g_count=0   #全作用域
def outer():
    o_count = 1
    def inner(): #
        i_count = 2
        print(o_count)
    inner()


def test():
    msg_inner = "I am from Runoob"
    for i in range(10):
        count = i
        print(i)
        print(msg_inner)
    print('Count is {0}'.format(count)) #count是局部變量，只有在函數內可以使用
test()


#global 和 nonlocal關鍵字
num = 1
def func1():
    global num
    print(num)
    num = 100
    print(num)

func1()
print(num)

def outer():
    num = 10
    def inner():
        nonlocal num
        num = 99
    inner()
    print("outer num is {0}".format(num))
outer()

try:
    a = 10
    def test():
        b = a+1
        #a = a+1
        print(a)
    test()
    print(a)
except:
    print("a 沒有被定義，他是區域參數！")
