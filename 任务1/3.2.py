#通过位置传递参数
def greet(name,time,sentence):
    return "Good "+time+", "+name+'. '+sentence
print(greet("Bob","morning","Nice to meet you."))
print("参数位置改变后：")
print(greet("morning","Bob","Nice to meet you.")) #通过函数括号内参数的顺序来匹配参数。当参数位置交换时,结果出人意料
print("-"*35)

#通过指定关键词传递参数
"""指定关键字值可以无需考虑调用函数时参数的位置"""
print(greet(time='Afternoon',sentence="Are you ok?",name='Cauchy'))
print("-"*35)

#编写函数时指定默认值
def greet_plus(name,time='evening',sentence="I miss you."):
    return ("Good "+time+", "+name+'. '+sentence)
print(greet_plus("Tom"))
"""对于存在默认值的参数，若无匹配的参数传递则使用默认的值，见下："""
print(greet_plus("Tom") == greet_plus("Tom",'evening','I miss you.'))

def sum1(first,*rest):
    print(type(rest))  #rest是一个元组
    sum = first
    print("first = " + str(first))
    for other in rest:
        sum += other
    return sum
print("Sum = " + str(sum1(1,2,3,4,5,6)))

def imformation(first_name,last_name,**others):
    print(type(others)) #**型变量为字典类型
    man = {}
    man['first_name'] = first_name
    man['last_name'] = last_name
    for key,value in others.items(): #可迭代
        man[key] = value
    return man

print(imformation('albert','einstein',sex='male',location='princeton',field='physics'))

