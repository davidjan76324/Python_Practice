import time
import calendar

ticks = time.time() #時間戳
print(ticks)
localtime = time.localtime() #时间元组
print(localtime)

#-- 格式化日期
#我们可以使用 time 模块的 strftime 方法来格式化日期：
date_format1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) #time.strftime(format, 时间元组)
print (date_format1)


# 将格式字符串转换为时间戳(时间元组(time.strptime()) → 时间戳(time.mktime()))
print (time.mktime(time.strptime(date_format1,"%Y-%m-%d %H:%M:%S")))
print(time.mktime(localtime))




cal = calendar.month(2016, 1)
print ("以下输出2016年1月份的日历:")
print (cal)