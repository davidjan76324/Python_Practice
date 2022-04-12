man = ["davidjan", 'David']
try:
    man_file = open('write.txt', 'w')

    for i in man:
        print(i, file=man_file) #file參數代表資料要存入何處？

except Exception as ex:  # 錯誤即會跳出
    print("--- Error Message: {0}".format(ex))
finally:  # 總是會執行區域！
    if 'man_file' in locals(): # locals()代表：會回傳定義於當前有效範圍的一群變數
        man_file.close()  # 不管怎樣，都會關閉檔案


#-- 利用with來處理檔案，可以免除finally 關閉檔案的需要
try:
    with open('write.txt', 'r') as data, open('sketch.txt', 'r') as sketch_data:
        print("---The write.txt info:")
        for info in data:
            print(info, end="")

        print("---The sketch.txt info:")
        for info_sketch in sketch_data:
            print(info_sketch, end="")
except Exception as ex:
    print("--- Error Message: {0}".format(ex))
