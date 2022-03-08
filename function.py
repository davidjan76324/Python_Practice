import myImport

def max(a, b):
    if a > b:
        return a
    else:
        return b


def change(a):
    print(id(a))  #10894368 :指向的是同一个对象
    a = 10
    print(id(a))  #10894656 : 一个新对象


a = 1
print(id(a))  #10894368
change(a)


def printinfo(name, age=35):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return


printinfo(age=50, name="runoob")
printinfo(name="runoob")


#不定长参数: tuple
def printinfo2(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print("printinfo2 - arg1: " + str(arg1))
    print(vartuple)  #加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。


printinfo2(70, 60, 50)


#不定长参数: Dictionary
def printinfo3(arg1, **vardict):
    "打印任何传入的参数"
    print("printinfo3 - arg1: " + str(arg1))
    print(vardict)  #加了两个星号 ** 的参数会以字典的形式导入。

printinfo3(70, a=2, b=3)




#Use import function
myImport.printInfo('fuck')
print(dir(myImport)) #内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回. 
print(dir()) #内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回.