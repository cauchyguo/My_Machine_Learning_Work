from threading import Thread
from random import randint
import time
def countdown(m):
    n = randint(1,10) #随机生成睡眠时间
    print("进程{}开始执行".format(m))
    while n > 0:
        print('进程{0}正在执行,剩余时间:{1}'.format(m,n))
        n -= 1
        time.sleep(1) #每执行一次循环,休眠一秒
    print("进程{}结束.".format(m))

t1 = Thread(target=countdown,args=(1,)) #建立一个Thread实例,跟踪目标为countdown函数,关键词args接受元组传递参数到函数
t1.start() #当调用start()方法,线程立即开始执行
t2 = Thread(target=countdown,args=(2,))

if t2.is_alive(): #通过is_alive()方法判断线程是否在执行
    print('Alive.')
else:
    print("Has not started.")
t2.start() #只有调用start()方法,Thread才正式开始执行
t2.join() #将t2加入到进程中
