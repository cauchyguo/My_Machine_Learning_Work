#元组的创建
a_tuple = (4,5,6,7)
#元组的访问
print(a_tuple)
print("a_tuple[2] =",a_tuple[2])#通过索引直接访问元组元素
for value in a_tuple:
    print(str(value) + '\t' ,end='')#通过for循环遍历元组元素
print('\n' + '——'*10)
#元组的不可修改性
try:  #使用try-except来检测元组能否修改
    a_tuple[2] = 0
except TypeError:
    print("a tuple one doesn't support modification")
else:
    print("a_tuple[2] =",a_tuple[2])