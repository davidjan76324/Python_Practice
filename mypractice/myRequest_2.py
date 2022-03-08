from urllib import request
import requests
headers = {
'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
"Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}


#-- get
request_get = requests.get("https://www.yahoo.com.tw", headers=headers)
print(request_get.text)

#-- post
#request_post = requests.post("http://siungsport.com/management/api/AccountApi/isMember",json = {"account":"davidjan","password":"123", 'groupIndex':1, 'isCheckPersonalInfo':1},headers=headers)
#print(request_post.status_code)
