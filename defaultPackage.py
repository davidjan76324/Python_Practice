import os
import shutil
import math
import random
import commonFunc
from datetime import date
import urllib
from urllib.request import urlopen
from urllib.parse import urlencode
from urllib.request import Request

#os
print(os.getcwd()) #目前資料夾
os.chdir('Server') # 修改当前的工作目录
#os.system('mkdir today')   # 执行系统命令 mkdir
os.chdir('/home/davidjan/Desktop/Python_Pracite')   # 修改当前的工作目录
os.system('ls')   # 展開資料

print(os.path.join(os.getcwd(),'Server'))


#shutil
#针对日常的文件和目录管理任务，:mod:shutil 模块提供了一个易于使用的高级接口:
#shutil.copyfile('SQL_connect.txt', 'SQL_connect2.txt')
#shutil.move('SQL_connect2.txt','Server')

#math
print(math.cos(math.pi / 4))

#random
randomChoice = random.choice(['apple', 'pear', 'banana'])
randomSample = random.sample(range(100),10)
randomRandom= random.random()
randomRandrange = random.randrange(6)
commonFunc.myPrint("randomChoice",randomChoice)
commonFunc.myPrint("randomSample",randomSample)
commonFunc.myPrint("randomRandom",randomRandom)
commonFunc.myPrint("randomRandrange",randomRandrange)


#日期和时间
"""
datetime模块为日期和时间处理同时提供了简单和复杂的方法。
支持日期和时间算法的同时，实现的重点放在更有效的处理和格式化输出。
"""
now = date.today()
birthday = "1987-03-24"
commonFunc.myPrint("Now",now)
commonFunc.myPrint("Birthday",birthday)
commonFunc.myPrint("Birthday Days",(now-birthday).days)


#urllib
"""
处理get请求，不传data，则为get请求
"""
url = "https://tw.yahoo.com/search"
data = {"p": "紙本五倍券", "fr": 'yfp-search-tn', "fr2": 'fp-hotsearch'}
req_data = urlencode(data)  #将字典类型的请求数据转变为url编码
res = urlopen(url + '?' + req_data)  #通过urlopen方法访问拼接好的url
res = res.read().decode()  #read()方法是读取返回数据内容，decode是转换返回数据的bytes格式为str
print(res)

"""
处理post请求,如果传了data，则为post请求
"""
# url = "https://tw.yahoo.com/search"
# data = {"p": "紙本五倍券", "fr": 'yfp-search-tn', "fr2": 'fp-hotsearch'}
# data = urlencode(data)  #将字典类型的请求数据转变为url编码
# data=data.encode('ascii')#将url编码类型的请求数据转变为bytes类型
# req_data=Request(url,data)#将url和请求数据处理为一个Request对象，供urlopen调用
# with urlopen(req_data) as res:
#     res=res.read().decode()#read()方法是读取返回数据内容，decode是转换返回数据的bytes格式为str

# print(res)
