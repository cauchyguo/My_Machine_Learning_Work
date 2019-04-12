import csv
import random
import math
from functools import reduce

class Kmeans:
    def __init__(self,file_name,k):
        self.k = k #聚类为K簇
        self.file_reader(file_name)
        self.set_meanvec() #随机生成初始k个均值向量
        self.H = [[] for i in range(k)]  #H装载k个分类簇

    def file_reader(self,file_name):#读取文件提取数据集
        self.D = [] #数据集dadaset
        with open(file_name, newline='') as csvfile:
            dataset = csv.reader(csvfile)
            for row in dataset:
                for i in range(len(row) - 1):
                    try:
                        row[i] = float(row[i])
                    except ValueError:
                        row[i] = str(row[i])
                    else:
                        pass
                self.D.append(row)



    def set_meanvec(self): #随机生成初始k个均值向量
        randomset = random.sample(range(len(self.D)), self.k) #在数据集中随机选取K个作为初始向量
        self.meanvector = []
        for i in sorted(randomset):
            self.meanvector.append(self.D[i])

    def avgC(self,C):
        """计算一个簇的所有样本的均值样本"""
        return reduce(self.avgc,C)#使用reduce来对簇内所有元素求平均

    def DBI(self):
        """计算DBI性能度量"""
        maxTmp = 0
        for i in range(self.k):
            maxI = 0
            for j in range(self.k):
                if i != j:
                    db = (self.avgdist(self.H[i])+self.avgdist(self.H[j]))/\
                         self.dist(self.avgC(self.H[i]),self.avgC(self.H[j]))
                    if db > maxI:
                        maxI = db
            maxTmp += maxI
        return maxTmp/self.k

    def DI(self):
        """计算DI性能度量"""
        diams = []
        dmins = []
        for k in range(self.k):
            diams.append(self.diam(self.H[k]))
        maxdiam = max(diams)
        for i in range(0,self.k - 1,1):
            for j in range(i + 1,self.k,1):
                it = self.dmin(self.H[i],self.H[j])
                dmins.append(it)
        mindmin = min(dmins)

        return mindmin / maxdiam

    def dmin(self,C1,C2):
        """求得两个簇之间的最小距离"""
        dmin_ = self.dist(C1[0],C2[0])
        for c1 in C1:
            for c2 in C2:
                distanse = self.dist(c1,c2)
                if distanse < dmin_:
                    dmin_ = distanse
        return dmin_

    def diam(self,C):
        """计算一个簇中两个任意两个分类样本的最大距离"""
        for i in range(len(C) - 1):
            diamC = self.dist(C[0], C[1])
            for j in range(i + 1, len(C)):
                d = self.dist(C[i], C[j])
                if d > diamC:
                    diamC = d
        return diamC

    def a_loop(self):
        """一次迭代"""
        for Ci in self.D: #迭代过程中为每一个样本根据与均值向量的最小距离聚类成簇列表(self.H)
            key = 0
            dis_min = self.dist(self.D[0],self.meanvector[0])
            for i in range(len(self.meanvector)):
                distance = self.dist(Ci,self.meanvector[i])
                if distance <= dis_min:
                    dis_min = distance
                    key = i
            self.H[key].append(Ci)

    def loop_for_n_times(self,n):
        """多重迭代""" #迭代的终止情况有1迭代此处到达指定次数2分类簇内的平均距离与上次差异不大(趋于稳定)
        for i in range(n):
            self.H = [[] for j in range(self.k)] #每次循环后重置k阶分类簇
            self.a_loop() #一次循环将测试集聚类
            test_mvc = self.meanvector[:]
            self.avgvecs() #将循环得到的簇求其均值向量
            if self.k * abs(self.avgdist(test_mvc) - self.avgdist(self.meanvector)) < 1e-10:
                break
        return i+1

    def avgvecs(self):
        """"根据聚类的簇,求得平均向量并将对应下标的均值限量覆盖"""
        self.meanvector = [] #重置均值向量
        for x in range(self.k):
            self.meanvector.append(self.avgC(self.H[x]))


    def dist(self,a, b):
        """计算两个样本a,b之间的距离度量"""
        i = s = 0
        while i < len(a):
            if type(a[i]) is float or type(a[i]) is int:
                s += (a[i] - b[i])**2
                i += 1
            else:
                break
        return math.sqrt(s)

    def avgdist(self,C):
        """计算一个簇的所有距离的均值"""
        s = t = 0
        for i in range(len(C) - 1):
            for j in range(i + 1, len(C)):
                s += self.dist(C[i], C[j])
                t += 1
        return s / t

    def avgc(self,a,b):
        """计算两个样本向量的均值样本向量"""
        i = 0
        c = []
        while i < len(a):
            if type(a[i]) is float or type(a[i]) is int:
                c.append((a[i] + b[i]) / 2)
            i += 1
        return c

    def show_result(self):
        """菜单函数,展示聚类结果"""
        print("测试数量：",len(self.D),"属性数量:",len(self.D[0]))
        print("聚类结果" + str(self.k) + "簇.")
        for i,h in enumerate(self.H):
            print("第{0}簇,数量为:{1}".format(i+1,len(self.H[i])))
        print("聚类后的均值向量:")
        for mv in self.meanvector:
            print(mv)
        print("DBI:",self.DBI(),"DI",self.DI())

file_name = "/home/ubuntu/PycharmProjects/Kmeans/venv/Data/winequality-red.csv"
test = Kmeans(file_name,k=5)
print("seeds数据集","迭代次数:",test.loop_for_n_times(n=10000))
test.show_result()
