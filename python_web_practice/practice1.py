#! /usr/bin/env python3
"""
在Linux/Unix系统中，你可以在脚本頂部添加以下命令讓Python脚本可以像SHELL脚本一样可直接執行：

#! /usr/bin/env python3

然後修改脚本權限，使其有執行權限，命令如下：
$ chmod +x practice1.py

執行以下命令：
$./practice1.py

"""


#--Python 使用反斜杠 \ 转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串：
import site
from typing import Dict


print("Ru\noob")
print(r"Ru\noob")

#--与 C 字符串不同的是，Python 字符串不能被改变, 会导致错误。
try:
    kk = "Hello world"
    kk[0] = "fuck"
except Exception as ex:
    print(ex)




#-- 列表(List)應用
listkk = ['abcd', 786, 2.23, 'runoob', 70.2]
tinyList = [123, 'runboob']
doubleTinyList = tinyList*2
print(doubleTinyList) # 输出两次列表 : list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
print(tinyList+listkk)  # 连接列表
print(listkk*2) # 重複兩次回傳list


a = [1, 2, 3, 4, 5, 6]
a[0:3] = ["gg","fuck","you"] #可直接取代; 修改元组(tuple)元素的操作是非法的
print(a) #['gg', 'fuck', 'you', 4, 5, 6]
print(a.pop()) #丟掉最後一個元素： ['gg', 'fuck', 'you', 4, 5]

names = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
new_names = [name.upper() for name in names if len(name) > 3]
print(new_names)


#List的遍历技巧
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers): #遍历技巧
    print("What is your {0}?  It is {1}.".format(q,a))




#-- set應用
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
if 'Google' in sites:
    print("Google 在集合中")
else:
    print("Google 不在集合中")

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a-b) # {'d', 'b', 'r'}

print(a.pop()) #set的pop是隨機移除一個

myset = { x for x in 'abracadabra' if x not in 'abc'}
print(myset) # {'r', 'd'}

myset.add("g") #新增一個
print(myset) # {'g', 'r', 'd'}

myset.update({'k','w'}) #一次新增多個
print(myset) # {'d', 'g', 'k', 'r', 'w'}

myset.update([1,2],[3,4])
print(myset) # {1, 'd', 2, 3, 4, 'g', 'w', 'k', 'r'}

myset.clear() #清除



#-- dictionary 應用
# 1、字典是一种映射类型，它的元素是键值对。
# 2、字典的关键字必须为不可变类型，且不能重复。
# 3、创建空字典使用 { }。
# #
dist = {}
dist["one"] = "1- practice"
dist["two"] = "2- practice"
print(dist)
print(dist.keys()) # dict_keys(['two', 'one'])
print(dist.values()) # dict_values(['2- practice', '1- practice'])

listdemo = ['Google','Runoob', 'Taobao']
newdict = {key:len(key) for key in listdemo}
print(newdict) #{'Taobao': 6, 'Google': 6, 'Runoob': 6}
print(len(newdict)) #算key的總數


#Dictionary 的遍历技巧： .items()
for k,v in newdict.items(): 
    print("key:{0}; value:{1}".format(k,v))


del newdict["Google"] #刪除其中一項
newdict.clear() #清空dictionary
del newdict #刪除dictionary


#-- tuple 應用
a = (x for x in range(1,10))
print(a)# 返回的是生成器对象
print(tuple(a)) # 使用 tuple() 函数，可以直接将生成器对象转换成元组

#元组中只包含一个元素时，需要在元素后面添加逗号 , ，否则括号会被当作运算符使用：
tup1 = (50)
print(type(tup1)) # <class 'int'>
tup1 = (50,)
print(type(tup1)) # <class 'tuple'>





#-- 運算
a = 21
b = 10
c = 0

c = a/b  # 相除
c = a//b  # 取整數
c = a % b  # 餘數



#-- Python身份运算符
# 注意：is 是用來判斷兩個id()是否相同( 就像： id(g) == id(k))
# 如果要比較兩個list等等，不適合用 「is」
# is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
g = [20]
k = [20]
print(id(g))
print(id(k))
if g == k:
    print("g == k")

if g is k:
    print("g is k")





#-- list(), tuple(), set(), dict() 的簡單宣告
mmylist = list((1,2,3,4))
mmytuple = tuple((1,2,3))
mmyset = set((1,2,3,4,5))
mmyDict = dict([("david",1),("mee",2)])
mmyDict2 = dict(david=1, mee=2)