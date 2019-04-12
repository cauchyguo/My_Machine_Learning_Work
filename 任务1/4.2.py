from datetime import datetime
today = datetime.today()
print(today)
birthday = datetime(1998,1,5)
print(birthday)
#datetime中的strftime方法将按照给定的占位符将datetime对象转化
today_form = today.strftime('%y-%m-%d,%H:%M,%A')
birthday_form = birthday.strftime('%A %B %d, %Y')
print(today_form,type(today_form)) #strfdate返回一个字符串类型
print(birthday_form)

from datetime import datetime
text = '1998-01-05'
birthday = datetime.strptime(text,'%Y-%m-%d') #将字符串按照其特有的格式将有效信息提取，生成datetime对象
print(birthday,type(birthday))
print(datetime.strftime(birthday,'%A, %B %d,%Y'))#datetime对象转化为字符串类型

from datetime import datetime
import csv #导入csv模块
file_name = 'sitka_weather_07-2014.csv'
dates = []
with open(file_name,'r')as f: #打开文件，制度模式
    reader = csv.reader(f) #将储存文件作为实参传递
    head_row = next(reader) #跳过源文件第一行的无效数据
    for row in reader:
        date_str = row[0] #提取每一行的时间字符串
        year,month,day = date_str.split('-') #通过split()方法将字符串分割成年月日
        dates.append(datetime(int(year),int(month),int(day)))#生成datetime对象并添加到列表中
for date in dates:
    print(date,type(date))

 #计算类似上周x的日期的问题
from datetime import datetime,timedelta
weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday',
            'Saturday','Sunday'] #申明星期一个列表
def get_previous_byday(dayname,start_date=None):
    if start_date == None: #若输入的其实时间为空,则通过today()获取当前时间
        start_date = datetime.today()
    day_num = start_date.weekday() #取得起始时间的星期对应的下标(周一～周日——>0～6)
    day_num_target = weekdays.index(dayname) #根据列表通过index()获取相应weekday对应的索引下标
    days_ago = (7 + day_num -day_num_target) % 7 #通过取余的方法求得今天与上周x相隔的天数
    if days_ago == 0: #若取余得7，正好说明相隔7天
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago) #起始日期减去datedelta类型的时间间隔得到上周x的datetime对象
    return target_date #将datetime返回

if __name__ == '__main__':
    today = datetime.today()
    print("今天日期：",today.strftime('%m-%d,%A')) #按格式输出日期
    last_Monday = get_previous_byday('Monday')
    print("上周一时间:",last_Monday.strftime('%m-%d,%A'))
    delta = datetime.today() - last_Monday
    print("相隔:",delta.days,'天') #调用函数，得到日期




