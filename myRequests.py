import requests 
#參考文件: https://blog.gtwang.org/programming/python-requests-module-tutorial/

headers = {
'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
"Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}


#--- 簡單的 Post & Get
#Get
result_get = requests.get('https://www.google.com.tw/', headers= headers)
print(result_get.status_code)
print(result_get.text)
print(result_get.content) #未解碼的二進位格式(bytes)

#Post
result_post = requests.post("http://siungsport.com/management/api/AccountApi/isMember", json = {"account":"davidjan","password":"123", 'groupIndex':1, 'isCheckPersonalInfo':1}, headers= headers)
print(result_post.status_code)
print(result_post.text)
