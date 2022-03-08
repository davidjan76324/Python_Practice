#-- type
#List
list = [1, 2, 3]
list2 = [2, 3, 4, 5]
list.append(4)
print(list)
print(list[0:len(list) - 1])
print(list + list2)

#Tuple
tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
print(tuple[0:len(tuple)])

#Set
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
thisset = set(("a", "b", "c"))
thisset.add("Facebook")
print(sites)  # 输出集合，重复的元素被自动去掉
print(thisset)
print(sites | thisset)  #聯集
print(sites & thisset)  #交集
thisset.remove("Facebook")  #移除元素
print(thisset)  #{'a', 'b', 'c'}

a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)  #{'r', 'b', 'd'}

#Dictionary
tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
tinydict["one"] = 2
del tinydict["one"]  #删除字典元素
print(tinydict)  #{'site': 'www.runoob.com', 'code': 1, 'one': 2, 'name': 'runoob'}
print(tinydict.keys())  # 输出所有键: dict_keys(['site', 'code', 'one', 'name'])
print(tinydict.values())  # 输出所有值: dict_values(['www.runoob.com', 1, 2, 'runoob'])
print({x: x**2 for x in (2, 4, 6)})  #{2: 4, 4: 16, 6: 36}
print(tinydict)

dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])  #tuple to dictionary
dict(sape=4139, guido=4127, jack=4098)

#if else
myifList = [1, 2, 3, 4]
myifList2 = [1, 2, 3, 4]
if 1 in myifList:
    print("Yes, 1 is in myifList!")
else:
    print("No, 1 is not in myifList!")

if myifList == myifList2:
    print("Yes,  myifList == myifList2!")
else:
    print("Yes,  myifList != myifList2!")


#Python 数字类型转换
mynum = "1"
int(mynum)  #1
tax = 12.5 / 100
price = 100.50
myTax = int(price * tax)  #12.5625
print("The Tax is =" + str(myTax))  #12

#Python3 字符串
var1 = 'Hello World!'
var2 = "Runoob"
print(var1[:])  #var1 = 'Hello World!'
print(var1[:6] + var2 + r"\n")  #Hello Runoob
print("我叫 %s 今年 %d 岁!" % ('小明', 10))  #我叫 小明 今年 10 岁!

mylist2 = ['Google', 'Runoob', "Zhihu", "Taobao", "Wiki"]
#del mylist2    #删除列表元素
print(mylist2[-1])  #Wiki

#for 遍历技巧
for i, v in enumerate(['tic', 'tac', 'toe']):  #enumerate 可以匯出list的 index, value
    print(i, v)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print("Key:{0}; Value:{1}".format(k, v))

#同时遍历两个或更多的序列，可以使用 zip() 组合：
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print("What is your {0}? It is {1}".format(q, a))
