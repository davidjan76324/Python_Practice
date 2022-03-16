def getFileInfo(fileName, sortType):
    try:
        myInfoList = []
        with open(fileName, 'r') as data:
            for info in data:
                myInfoList = myInfoList + list(map(float, info.strip().replace(':', '.').replace('-', '.').split(',')))
            print("--- File:{0}".format(fileName))
            print(mysortList(sortType, myInfoList, True)['Msg'])
            print(sorted(set(mysortList(sortType, myInfoList, True)['Msg']))) #利用set去除重複的&排序

    except Exception as ex:
        print("--- Error Message: {0}".format(ex))


def mysortList(type: str, mylist: list,reverse:bool):
    try:

        if isinstance(mylist, list):
            if type == 'sort':
                mylist.sort(reverse=reverse) #破壞性的sort (ln-place Sorting, 就地排序)
                return retunInfo(200, mylist)
            elif type == 'sorted':
                return retunInfo(200, sorted(mylist,reverse=reverse)) #非破壞性的sort (Copied Sorting, 複製排序)
            else:
                return retunInfo(200, mylist)

        return retunInfo(500, "mylist is not list class!")
    except Exception as ex:
        return retunInfo(500, "--- Error:{0}".format(ex))


def retunInfo(code: int, msg: str):
    return {'Code': code, "Msg": msg}


getFileInfo('james.txt', 'sort')
getFileInfo('sarah.txt', 'sort')




#-- List Comprehension
numbers = listCom = []
for x in range(10):
    numbers.append(x * 3)
print(numbers)

listCom = [x*3 for x in range(10) if x > 4]  # List Comprehension
print(listCom)


#-- list slice 清單切片
print(listCom[0:3])


#-- Method chaining(方法鍊結)
def showMyList(mylist):
    return  " ".join(mylist)
print(showMyList(["fuck","you"]).upper())

#-- function chaining(函式鍊結)
def showList():
    return sorted

mmList = [2,22,3,123]
print(showList()(mmList))