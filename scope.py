# 注意：
# Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
# 其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域！！

g_count = 0  # 全局作用域
def outer():
    o_count = 1  # 闭包函数外的函数中
    def inner():
        i_count = 2  # 局部作用域



def test():
    msg_inner = 'I am from Runoob' #它是局部变量，只有在函数内可以使用。
    for i in range(10):
        count = i # 其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域！！
        print(i)
    print('Count is {0}'.format(count)) #count 它是局部变量，只有在函数内可以使用。

test()



#global 和 nonlocal关键字
num = 1
def func1():
    global num
    print(num) #1
    num = 100
    print(num) #100

func1()
print(num) #100

def outer():
    num = 10
    def inner():
        nonlocal num
        num = 100
        print(num) #100
    inner()
    print(num) #100
outer()



try:
    a = 10
    def test():
        a = a + 1
        print(a)
    test()
except:
    print("a 沒有被定義，他是區域參數！！")