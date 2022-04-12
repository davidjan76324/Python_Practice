import json

data = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}

# -- dictionary to json
json_string = json.dumps(data) # {"no": 1, "name": "Runoob", "url": "http://www.runoob.com"}
print(json_string)


# -- json to dictionary
data = json.loads(json_string)
print(type(data))
print(data)
print('--- the data name = {0}'.format(data['name']))


"""
Hint:
    w：覆蓋寫入模式，寫入後原本檔案的內容會被覆蓋掉。
    a：附加寫入模式，寫入的資料會附加在原本檔案內容的後面。
"""
with open('myJson.txt', "a") as f:
    print(json.dumps(data), file=f)  # file參數代表資料要存入何處？
    # json.dump(data,f) #json.dump 用來寫入檔案用


with open('myJson.txt', "r") as f:
    #mydata = json.load(f)
    for i in f:
        mydata = json.loads(i)
        print(mydata)
