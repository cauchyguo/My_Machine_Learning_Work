student = {'name':'Cauchy','ID':'2016212074','dept':'CS'} #建立一个字典对象
#字典的访问
print(student['name'])            #通过键访问值
for key,value in student.items(): #items()方法返回一个键值对元组列表,通过for-in 即可遍历字典的内容
    print(key,value)              #keys,values等方法与items相似
#键值对的添加与修改
student['sex'] = 'man'            #通过指明键来对字典进行添加和修改
student['dept'] = 'IS'
print(student)

#字典键值对的删除
del student['sex']                #使用del即可将字典的键及其对应的值删除
print(student)

user = {
    'user_name':'Cauchy',
    'first_name':'Tom',
    'last_name':'Kobe',
}
for key,value in user.items():
    print('key:' + key)
    print('value' + value)

lists = ['user_name','first_name','last_name']
for list in lists:
	print(list,user[list])

#通过OderedDict模块使字典有序
from collections import OrderedDict
user = OrderedDict()
user['user_name'] = 'Cauchy'    #OrderedDict内部维护了一个双向链表,会根据元素添加进来的顺序排列键的位置
user['first_name'] = 'Bob'      #但是这种做法几乎使字典的存储空间翻倍
user['last_name'] = 'Kobe'
for key, value in user.items():
    print(key,value)
print('-'*20)
#通过defaultdict模块使字典的键映射多个值(列表list或集合set)
from collections import defaultdict
d = defaultdict(list)
d['a'].append([1,2,4])  #添加多个值到'a'键
d['b'].append(5)
for key,value in d.items():
    print(key,value)
e = defaultdict(set)
e['a'].add(1)
e['a'].add(1)   #集合的唯一性
e['b'].add(3)
print(e)
#字典推导式
"""字典的keys()方法返回key-viem对象,由此可对keys()对象做类集合运算,交并差对称等运算"""
print('-'*20)
a = {2:2,3:3,4:4}
b = {1:2,2:3,3:3}
print(a.keys()&b.keys())  #结果返回一个集合包含两者的交集
c = {key:a[key] for key in a.keys() & b.keys() } #通过字典推导式可得a中与b都存在的键的新字典
print(c)
