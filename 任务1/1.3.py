#简单申明几个列表变量
names = ['Bob','Tom','Cauchy','Lucy']
students = [{'name':'Tom','age': 19,'location':'HuBei'},
            {'name':'Cauchy','age': 20,'location':'JiangXi'}]

numbers = list(range(1,10))#通过range()函数生出一系列有规律的数字,再由list()函数列表化
value_square = [value**2 for value in range(0,10)] #一个简单的列表解析

#列表的访问
print(numbers)#直接print出列表
print(value_square)

for student in students:#通过for循环遍历列表元素
    print(student['name'] + ', who aged ' + str(student['age']) +
          ', is from ' + student['location'] + '.')

print(names[0],names[2])#通过索引直接访问列表元素
q
#列表的添加
names = []#申明一个空列表
names.append('Tom')#通过append()从列表末尾添加元素
names.append('Bob')
names.insert(0,'Cauchy')#通过insert()可通过指定索引来插入元素
names.insert(1,'Mike')
print(names)
#列表的删除
value = 2
del names[value] # del语句可通过指定列表的元素索引来删除相应的元素
print(names)
guy = names.pop(value)#pop()方法可通过指定列表元素的下标来删除指定，默认在不带参数的情况下弹出最后一位,pop()方法返回弹出的元素值
print(guy,names)
names.remove('Mike')#remove方法可在不知道元素具体的情况下,根据元素的值来删除元素
print(names)

#列表切片
subjects = ['Maths','Eghlish','Chinese','PE','Arts','OS']
""""通过对已有的列表指定其起始索引与终点索引来切片得到新的列表。[:]表示切片所有的元素(可用以复制列表)
与列表的索引相同，切片只截取到终点索引前一位"""
major_subjects = subjects[0:4]
elective_subjects = subjects[-2:] #当索引值为负数(-n)时表示倒数第n个值
print("major subject: {0},elective subjects: {1}".format(major_subjects,elective_subjects))
#分解列表元素
#对于可迭代对象如列表,可将一系列变量配合*来分解迭代对象,提取有效信息
record = "Cauchy,cauchyguo@gmail.com,Chongqing,17723084945,cs"
name, mail, *hehe, depart = record.split(',') #
print(name,mail,depart)
#列表加法与乘法
"""列表和字符串一样支持加法与乘法"""
numbers = list(range(1,6))
nums1 = numbers + numbers
nums2 = numbers * 2
print(nums1,nums1 == nums2)
print(list(set(nums1))) #对于列表去除重复,可以用set()函数转化为集合再通过list()转化为列表
#通过Counter类来统计列表元素的出现次数
from collections import Counter
sentences = "jdaiojdoaoidajojdoajojdoeqwqajsijiajoeokd"
words = [s for s in sentences]#将字符串分解成单字符组成的列表
objectC = Counter(words)# 建立一个Couter类
top_three = objectC.most_common(3)#调用Couter类中most_common()方法查找频率最高的三个元组并返回列表元组
print(top_three)
