import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",       # 数据库主机地址
  user="root",    # 数据库用户名
  passwd="parallels",   # 数据库密码
  database="TestPython"
)
mycursor = mydb.cursor()


#-- Select
mycursor.execute("SELECT * FROM `Members`")
# for x in mycursor:
#     print(x)

myresult = mycursor.fetchall()  # fetchall() 获取所有记录; fetchone():读取一条数据
for x in myresult:
    print(x)

#-- Insert
# mycursor.execute("INSERT INTO `Members`(`Name`, `Age`, `serialNo`) VALUES ('{0}',{1},null)".format("Mee",17))
# mydb.commit()    # 数据表内容有更新，必须使用到该语句
# print(mycursor.rowcount, "记录 Insert成功。")


#-- Update
mycursor.execute("UPDATE `Members` SET `Name`='{0}' WHERE `serialNo` = 1".format("Alice"))
mydb.commit() 
print(mycursor.rowcount, "记录 Update成功。")