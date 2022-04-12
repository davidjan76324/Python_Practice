
#-- for的特殊用法
sites = ["Baidu", "Google","Runoob","Taobao"]

for i,site in enumerate(sites):
    print(i)
    if site == "Google":
        print('Each site is Google')
else:
    print("全部執行完之後，才會執行else這塊，如果中途从break跳出，则连else一起跳出！")






#-- python 函数的参数传递：
"""
a.不可变类型：类似 C++ 的值传递，如整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。
如果在 fun(a) 内部修改 a 的值，则是新生成一个 a 的对象。

b.可变类型：类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响
"""
# 可写函数说明
def changeme( mylist ):
   "修改传入的列表"
   mylist.append([1,2,3,4])
   print ("函数内取值: ", mylist) #[10, 20, 30, [1, 2, 3, 4]]
   return
 
# 调用changeme函数
mylist = [10,20,30]
changeme( mylist )
print ("函数外取值: ", mylist) #[10, 20, 30, [1, 2, 3, 4]]



