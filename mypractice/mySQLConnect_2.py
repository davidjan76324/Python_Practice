import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",       # 数据库主机地址
  user="root",    # 数据库用户名
  passwd="parallels",   # 数据库密码
  database="TestPython"
)

mycursor = mydb.cursor()




#-- select
mycursor.execute("select * from Members")
for i in mycursor:
    print(i)


#-- update
mycursor.execute("UPDATE `Members` SET `Name`='{0}' WHERE `serialNo` = 1".format("DavidJan"))
mydb.commit()
print(mycursor.rowcount)