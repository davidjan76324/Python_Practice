#--- 不定长参数(tuple)
def printInfo(arg1, *vartuple):
    print("輸出：")
    print(arg1) #1
    print(vartuple) #(2,3)
printInfo(1,2,3)


#--- 不定長參數(dict)
def printInfo_dict(arg1, **varDict):
    print("Out:")
    print(arg1) #10
    print(varDict) # {'b': 12, 'a': 11}

printInfo_dict(10,a=11,b=12)



def f(a,b,*,c):
    return a+b+c
print(f(1,2,c=3)) #如果单独出现星号「*」后的参数必须用关键字传入。


#-- lambda
#语法
#lambda 函数的语法只包含一个语句，如下：
'''
    lambda [arg1 [,arg2,.....argn]]:expression
'''
sum = lambda x,y:x+y
print(sum(10,3))

def myfunc(n):
    return lambda a: a**n
mydoubler = myfunc(2) #lambda a: a**2
print(mydoubler(10))
