from datetime import timedelta,datetime
a = timedelta(days=2,hours=4)
b = timedelta(hours=5)
c = a - b
print(c,type(c)) # datedelta类型可由datedelta类型相加减得到
print(c.days,c.total_seconds()) #datedelta类型有days,seconds等属性,total_seconds则为所有单位换算为秒的总数值
d = datetime.now()
e = d + a
print(type(e)) # datedelta类型与datetime类型相加减得到datetime类型对象

from datetime import date
birthday = date(1998,1,5)
today = date.today()     #date中today方法根据time.time()返回当前时间信息
print(today)
print(birthday)
delta = today - birthday
print(delta,type(delta)) #date对象相减得到datedelta对象

from datetime import datetime
today = datetime.today() #today方法返回当前时间并精确到微秒
print(today)
utctime = today.utcnow()
delta = today - utctime #北京时间一般为utc + 8小时
print(delta,type(delta))  #相减得到timedelta对象


