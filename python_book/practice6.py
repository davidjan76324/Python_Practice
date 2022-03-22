from multiprocessing import connection
import sqlite3
conn = sqlite3.connect('example.db')
"""
connect():建立一條連線到資料庫
cursor(): 通過既有連線與資料庫通訊
execute(): 將sql查詢送往資料庫
commit():對資料庫進行永久變更
colse():關閉連線

"""

#-- 創建 table: contacts
# c = conn.cursor()
# c.execute("CREATE TABLE contacts (date text, name text, number text)")
# conn.commit()
# conn.close()

#-- insert to contacts table
# conn = sqlite3.connect('example.db')
# c = conn.cursor()
# c.execute("INSERT INTO contacts VALUES ('2018-03-11','王小寶','222')")
# c.execute("INSERT INTO contacts VALUES ('2018-03-12','吳有明','321')")
# c.execute("INSERT INTO contacts VALUES ('2018-03-15','白采君','320')")
# conn.commit()
# conn.close()

#-- select all from contacts table
conn = sqlite3.connect('example.db')
c = conn.cursor()
for row in c.execute('SELECT * FROM contacts ORDER BY number'):
    print(row) #tuple
    print("Date:{0}; Name:{1}; number:{2}".format(row[0],row[1],row[2]))

conn.close()


#-- insert to other table(testTable)
# conn = sqlite3.connect('example.db')
# c = conn.cursor()
# c.execute("INSERT INTO testTable VALUES (null,'0985200505')")
# conn.commit()
# conn.close()




#-- functions
def getMyDBInfoByQuery(dbName, queryString):
    try:
        conn = sqlite3.connect(dbName)
        c = conn.cursor()
        infos = c.execute(queryString)

        #for info in infos:
        #    infoList.append(info)
        infoList = infos.fetchall() #fetchall()：取出全部資料; fetchone()：取出第一筆資料
        conn.close()
        return {'Code': 200, "Msg": infoList}  # [(),()...]
    except Exception as ex:
        return {'Code': 500, "Msg": ex}


def setMyDBInfoByQuery(dbName):
    try:
        conn = sqlite3.connect(dbName)
        c = conn.cursor()
        c.execute("INSERT INTO contacts VALUES (?,?,?)",('2022-03-11','Davidjan','222')) # "?" 佔位符：讓你可以在python程式碼中將SQL陳述句參數化
        conn.commit()
        conn.close()
        return {'Code': 200, "Msg": ''} 
    except Exception as ex:
        return {'Code': 500, "Msg": ex}

kk = getMyDBInfoByQuery('example.db','SELECT * FROM contacts ORDER BY number')
print(kk)

#setMyDBInfoByQuery('example.db')
