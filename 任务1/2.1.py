msg = "How old are you?" #输入提示
msg += "\nage:"
age = int(input(msg)) #将输入的字符整型化
#多重if-elif-else判断语句
if 0 < age and age < 18:
    print("You are a minor.")
elif 18 <= age and age < 35 :
    print("You are a adult.")
elif 35 <= age and age < 60:
    print("You are a middle-aged person.")
elif age >= 60:
    print("You are the old.")
else: #当输入的数据不在有效范围内,坚持使用else以加强程健壮性
    print("You are strange man.")

def func0():
    print('This is the default function.')
def func1():
    print('This is function 1.')
def func2():
    print('This is function 2')
def func3():
    print('This is function 3')

functions = {
    0:func0,
    1:func1,
    2:func2,
    3:func3,
}
menu = 'which function do you want to run\n' #生成人性化菜单
menu += '1 -> func1\n2 -> func2\n3 -> func3\n'
menu += 'choice:'
choice = int(input(menu)) #将字典的键数值化
#字典的get方法通过传递的第一个参数查找并返回指定的键的值,若不存在则返回default参数的值(default默认为none)
functions.get(choice,func0)()

#for循环
for value in range(0,11,2): #0-10之间的偶数
    print(value,' ',end='')
print()
print('-'*20)

#while循环
Test = True
lists = []
while Test: #在while语句中通常设置一个标签，通过修改标签的真假的决定退出循环
    words = input("Input a word('quit' to leave)\nwords:")
    if words.lower() != 'quit': #字符串的lower方法使字符串的字符全部改为小写与之相反的时upper方法
        lists.append(words)
        continue #continue语句一旦执行之间跳过单次循环的剩余语句直接执行下一次循环
    else:
        Test = False #此句效果等价与break,间接的退出了循环
for list in lists:
    print(list,' ',end='')