#Write file
f = open('SQL_connect.txt', "a+")
f.write("Python 是一个非常好的语言。是的，的确非常好!!\n")

f.close()

#Read file
#关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法(Ex: 關閉連結):
try:
    with open('SQL_connect.txt', "r+") as fr:
        for line in fr:
            print(line)
except:
    print('---Read File Error!')


def this_fails():
    x = 1 / 0


