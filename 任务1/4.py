#列表推导式 使用[]生成列表
odds = [x for x in range(1,30) if x % 2 is 1] #列表推导式
print(odds,type(odds)) #查看类型
#列表推导式支持多重for循环
a = [[1,2,3],[3,4,5],[5,6,7],[7,8,9]]
nums = [x**2  for i in a for x in i]
print(nums)
#模拟掷骰子实验
from random import randint
from collections import Counter
experiment = [randint(1,6) for i  in range(10000)] #生成一万次的随机实验
nums_count = Counter(experiment) #使用Counter来统计实验
results = nums_count.most_common(6)
for r in sorted(results,key=lambda x:x[0]):
    print(r[0],':',r[1] ,'{:.2%}'.format(float(r[1]/10000)))
#字典推导式 使用{}生成字典
names = ['Bob','Tom','Lucy','Cauchy']
height = [172,163,152,175]
student_h = {x : y for x in names for y in height}
print(student_h)



