add = lambda x,y:x + y
print(add(5,6))
print(add('hello','world'))
#lambda常用于sort排序的关键词
students = [
    {'name':'bob','grades':79},
    {'name':'tom','grades':80},
    {'name':'cauchy','grades':84},
]
print("按成绩高低排序")
for student in sorted(students,key=lambda student:student['grades'],reverse=True):
    print(student)  #lambda后的student为列表的元素,冒号后为表达式返回的结果,key的实参
print("按名字首字母排序")
for student in sorted(students,key=lambda student:student['name']):
    print(student)