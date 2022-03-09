man = ["davidjan",'David']
try:
    man_file = open('write.txt','w')

    for i in man:
        print(i, file=man_file)

except Exception as ex: #錯誤即會跳出
    print("--- Error Message: {0}".format(ex))

finally: #總是會執行區域！
    if 'man_file' is locals():
        man_file.close() #不管怎樣，都會關閉檔案


#-- 利用with來處理檔案
