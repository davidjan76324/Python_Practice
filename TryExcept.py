#function內也抓的到error
try:
    this_fails()  #function內也抓的到error
except:
    print("--- Error!")


def runboob():
    print('runboob!!')


#try... except... else... finally
try:
    runboob()
except:
    print("--- runboob is Error!")
else:
    try:
        frr = open('SQL_connect.txt', "r+")
        for line in frr:
            print(line)
    except:
        print('---Read File Error!')
finally:
    print('句话，无论异常是否发生都会执行。')

#raise: Python 使用 raise 语句抛出一个指定的异常。
try:
    print("Use raise!")
    raise
except:
    print("--- Use raise, this is Error!")

x = 10
#if x > 5:
#    raise Exception('x 不能大于 5。x 的值为: {0}'.format(x))


#raise 唯一的一个参数指定了要被抛出的异常。
try:
    raise NameError("HiThere")
except NameError:
    print("An exception flew by!")