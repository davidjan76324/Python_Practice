#--- dictionary(字典)
name_dict = dict()
name_dict["Name"] = "Davidjan"
name_dict["occupations"] = ["actor", "comedian", "writer"]
print(name_dict)  # {'Name': 'Davidjan'}


#-- class(類別)
#方法(Method)可以共享, 屬性(Attribute)無法共享
class Athlete:
    def __init__(self, value: str):  # self:可以指出所要處理的是哪個物件實例資料
        self.thing = value

    def how_big(self):
        if isinstance(self.thing, str):
            print(
                "-- the value={0}; len = {1}".format(self.thing, len(self.thing)))
        else:
            print("the value is not string!")


a = Athlete("Fuck you!")
a.how_big()
