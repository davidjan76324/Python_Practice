def getFileInfo(fileName, sortType):
    try:
        myInfoList = []
        with open(fileName, 'r') as data:
            for info in data:
                myInfoList = myInfoList + \
                    list(map(float, info.strip().replace(':', '.').replace('-', '.').split(',')))
            print("--- File:{0}".format(fileName))
            print(mysortList(sortType, myInfoList)['Msg'])

    except Exception as ex:
        print("--- Error Message: {0}".format(ex))


def mysortList(type: str, mylist: list):
    try:

        if isinstance(mylist, list):
            if type == 'sort':
                mylist.sort() #破壞性的sort
                return retunInfo(200, mylist)
            elif type == 'sorted':
                return retunInfo(200, sorted(mylist)) #非破壞性的sort
            else:
                return retunInfo(200, mylist)

        return retunInfo(500, "mylist is not list class!")
    except Exception as ex:
        return retunInfo(500, "--- Error:{0}".format(ex))


def retunInfo(code: int, msg: str):
    return {'Code': code, "Msg": msg}


getFileInfo('james.txt', 'sort')
getFileInfo('sarah.txt', 'sort')
