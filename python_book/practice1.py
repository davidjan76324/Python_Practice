names=["david","mee"]
if isinstance(names,list): #辨別型態
    print("yes, name is list!")


#python Package Index(pyPI)，替第三方python模組在Internet上提供了一個中央儲存庫。當你準備妥當之後，也可以透過PyPI來發布你的模組，讓其他人也能使用你的模組。


#-- 命名空間：匯入模組時，會以模組的名稱當作命名空間
#python主要的命名空間，就是大家知道的：__main__
#from myModel.demo import showHello
from myModel import demo 
demo.showHello() #__name__: myModel.demo


import model_1 
model_1.showHello() #__name__: model_1

import sys
print(sys.path) #python只會到路徑清單中尋找模組
#路徑清單：['/home/davidjan/Desktop/Python_Pracite/python_book', '/usr/lib/python35.zip', '/usr/lib/python3.5', '/usr/lib/python3.5/plat-x86_64-linux-gnu', '/usr/lib/python3.5/lib-dynload', '/home/davidjan/.local/lib/python3.5/site-packages', '/usr/local/lib/python3.5/dist-packages', '/usr/lib/python3/dist-packages']
#如果你擺放模組的資料夾並未列在python的路徑清單中，直譯器找不到，這會導致ImportErrors的結果。



# enumerate(), range(), id()...
# BIF(built-in function, 內建函式)都會被特別匯入每個python內！
#
for i,v in enumerate(["david", "jan"]):
    print("i:{0}; v:{1}".format(i,v),end="\t")

for i in range(3):
    print("i:{0}".format(i),end="\t")

myName = "davidjan"
print("myName id is {0}".format(id(myName))) #識別碼

try:
    showFuck()
    def showFuck():
        print('Fuck')
except Exception as ex:
    print(ex)



#【 注意： 规定默认值时，不一定要声明变量所属的类型，
# Python是一门动态语言，它总会在Python解释器进程运行的时候去动态地判定一个变量赋值的类型，
# 而之所以在代码中声明静态类型则是为了减少人为错误而提供相应的类型或错误提示，但并不会影响Python的运行！】
# Ref: https://blog.csdn.net/qq_44683653/article/details/108990873
def foo_v1(a:int, b:int=1): #默認參數b = 1
    print(a+b)

foo_v1(a=1) #尚未給b傳入參數, 採用默認值