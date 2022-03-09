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

