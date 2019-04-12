#集合的创建
a = set(['a','b','c','d']) #创建一个数值集合
string = 'apple'
s = set(string)   #创建一个字符集合
#集合的性质
for c in a:
    print(c,end='') #集合支持for-in遍历,但是输出不确定(集合的无序性)
print()
print(len(string ),len(s)) #集合自动消除重复元素,集合的唯一性
print('-'*30)
#集合的操作
a.add('x')                  # add()添加一项
print("a添加一项后：",a)
a.remove('x') #remove()移除一项
print("a移除一项后：",a)
s.update(['m','n'])         #update()添加多项
print("s一次添加多项后：",s)
s.clear()                   #clear()将集合清零
print(s)
s = set(string)
print('-'*30)
#集合的数学运算
print('s:',s,'\t','a:',a)
print('s - a =',s-a)    #求集合的差集
print('s | a =',s|a)    #求集合的并集
print('s ^ a =',s^a)    #求集合的对称差集(同时不在两集合中的元素集合)
print('s & a =',s&a)    #求两集合交集