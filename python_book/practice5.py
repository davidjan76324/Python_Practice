#--- dictionary(字典)
name_dict = dict()
name_dict["Name"] = "Davidjan"
name_dict["occupations"] = ["actor", "comedian", "writer"]
print(name_dict)  # {'Name': 'Davidjan'}


#-- class(類別)
# 方法(Method)可以共享, 屬性(Attribute)無法共享
# 屬性：就是存在物件實例中的變數
# __init__:可以定義在類別中，用於初始化物件實例
class Athlete:
    #定义基本属性
    ii = 123 
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self, value: str):  # self:可以指出所要處理的是哪個物件實例資料
        self.thing = value

    def how_big(self):
        if isinstance(self.thing, str):
            print("-- the value={0}; len = {1}".format(self.thing, len(self.thing)))
            print("iii = {0}".format(self.ii)) 
            print("__weight = {0}".format(self.__weight))
        else:
            print("the value is not string!")


a = Athlete("Fuck you!")
a.how_big()
