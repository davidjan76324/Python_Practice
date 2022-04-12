#-- 開檔讀檔案
data = open('sketch.txt')
# print(data.readlines())

for i in data:
    print(i.replace('\n', ''))

data.close()  # 關閉讀檔


#-- 例外(exception)
try:
    myStr = 'Man:Is this the right room: for an argument?'
    [role, line_spoken] = myStr.split(':', 1) # 額的引數用於控制split的分割幾個部份, max split = 1
    print(role)  # ['Man', 'Is this the right room: for an argument?']
    print(role[5])
except Exception as ex:
    print("--- Error Msg: {0}".format(ex))


#使用 else 子句比把所有的语句都放在 try 子句里面要好，这样可以避免一些意想不到，而 except 又无法捕获的异常。
try:
    print("try: 執行代碼區域！")
except Exception as ex:
    print("except: 異常就執行的區域！")
    print("--- Error Msg: {0}".format(ex))
else:
    print("else: 沒有異常執行就執行else！")
finally:
    print("finally: 不管有沒有異常都會執行finally！")

#Hint: 异常处理并不仅仅处理那些直接发生在 try 子句中的异常，而且还能处理子句中调用的函数（甚至间接调用的函数）里抛出的异常。例如:
def this_fails():
    x = 1/0
try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)



# -- find()：判斷有無找到誇號內的字串
print(myStr.find('Hello'))  # -1
print(myStr.find(':'))  # 3

try:
    mydata = open('hello.txt')
    print(mydata.readlines())
    mydata.close()
except Exception as ex:
    print("--- Error Msg: {0}".format(ex))



#-- is 和 is not介紹
#is not : !=
#is : ==
myvalue = 1
if myvalue is not 2:
    print("test")
