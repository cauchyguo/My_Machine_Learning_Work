students = [
    {'name':'bob','grades':79},
    {'name':'tom','grades':80},
    {'name':'cauchy','grades':84},
    {'name':'mike','grades':84}
]
def list_students(students,sort_key=''):
    print("Sort by",sort_key,':')
    print('\tname\tgrades')
    for student in students:
        print('\t{:<8} {}'.format(student['name'].title(),student['grades']))
#若想通过学生的名字字母永久顺序排序，使用list()
students.sort(key=lambda student: student['name'])
list_students(students,"name")
#若想对学生按照分数临时从高到低排序(做菜单式输出)
list_students(sorted(students,key=lambda student:student['grades'],reverse=True),'grades')
#检查列表实际有无变化
list_students(students) #结果与第一次输出相同
#可同时指定多个key,比如按分数，姓名排序
list_students(sorted(students,key=lambda student:(student['grades'],student['name']),
                     reverse=True),'grades and name')

from operator import itemgetter
students = [
    {'name':'bob','grades':79},
    {'name':'tom','grades':80},
    {'name':'cauchy','grades':84},
    {'name':'mike','grades':84}
]
def list_students(students,sort_key=''):
    print("Sort by",sort_key,':')
    print('\tname\tgrades')
    for student in students:
        print('\t{:<8} {}'.format(student['name'].title(),student['grades']))

#若想通过学生的名字字母永久顺序排序，使用list()
students.sort(key=itemgetter('name'))
list_students(students,"name")
#若想对学生按照分数临时从高到低排序(做菜单式输出)
list_students(sorted(students,key=itemgetter('grades'),reverse=True),'grades')
#检查列表实际有无变化
list_students(students) #结果与第一次输出相同

from functools import reduce
from random import randint #导入随机数模块
#对数值列表求和
nums = list(range(1,10))
print(nums)
sum = reduce(lambda x,y:x+y,nums)
print(sum)
from random import randint #导入随机数模
random = set()
for x in range(0,15): #生成是个随机数组
    random.add(randint(0,100))
print("集合：",random,"长度：",str(len(random)))
#找出集合中的最大数
max = reduce(lambda x,y:x if x > y else y,random) #对集合中的元素进行遍历比较
print("最大数：",str(max))

from random import randint #导入随机数模
#找出偶数
nums = list(range(-6,3))
odds = list(filter(lambda x:x % 2 == 0,nums))
print(nums,odds)
#从集合中找出质数
def find_prime_number(x):
    for i in range(2,int(x/2)):#质数判断
        if x % i == 0:
            return False
        return True
if __name__ == '__main__':
    random = set()
    for x in range(0, 15):  # 生成是个随机数组
        random.add(randint(0, 100))
    print("集合：", random, "长度：", str(len(random)))
    _ = filter(find_prime_number,random)
    print(type(_))#filter函数生成一个filter对象
    prime_nums = set(_)
    print("质数：",prime_nums)
