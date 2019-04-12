from collections import Counter
import csv
import heapq
import random
import math
class KNN:
    def __init__(self, file_name, k):
        self.k = k  #
        self.file_reader(file_name)

    def file_reader(self, file_name):  # 读取文件提取数据集
        """读取文件信息同时通过留出法划分好训练集和测试集"""
        self.Dataset = []  # 原始数据集
        with open(file_name, newline='') as csvfile:
            _ = csvfile.readline()
            data = csv.reader(csvfile)
            for row in data:
                for i in range(len(row)):
                    try:
                        row[i] = float(row[i])
                    except ValueError:
                        row[i] = str(row[i])
                    else:
                        pass
                self.Dataset.append(row)
        self.testSet = random.sample(self.Dataset,10) #sample函数从原始数据集中随机取得10个样本作为测试集
        self.D = []
        for sample in self.Dataset: #将原始数据集中的其他示例添加到训练集中
            if sample not in self.testSet:
                self.D.append(sample)

    def dist(self, a, b):
        """计算两个样本a,b之间的欧式距离"""
        i = s = 0
        while i < len(a):
            if type(a[i]) is float or type(a[i]) is int:
                s += (a[i] - b[i]) ** 2
                i += 1
            else:
                break
        return math.sqrt(s)

    def majorLabel(self, classList):
        """函数用于统计某个样本集下类别数最多的类别"""
        statistical = Counter(classList)  # 使用Counter类来统计比例最高的类
        majorLabel = statistical.most_common(1)
        return majorLabel[0][0]

    def classifyLabel(self,sam,regression=False):
        '''通过regreession来决定执行什么任务（回归或分类）'''
        distances = []
        for sample in self.D:
            distances.append(self.dist(sam,sample))
        L = heapq.nsmallest(self.k,distances) #heapq堆模块可方便寻得最小的k个距离
        classLabels = [self.D[i][-1] for i in range(len(self.D)) if distances[i] in L ]
        if regression: #回归任务
            avg_label = 0
            for x in set(sorted(classLabels,reverse=True)):
                avg_label += (classLabels.count(x)) / (float)(len(classLabels)) * x #求得加权平均数
                return avg_label
        else:
            return self.majorLabel(classLabels) #返回标签类别列表中的多数标签

    def test(self,file_name):
        regression = False #通过示例样本的最后一位属性值的属性确定KNN任务
        print("数据集",file_name,"评估方法: 留出法")
        # if type(self.testSet[0][-1]) is str:#若为字符，即为回归任务
        #     regression = False
        #     print("分类任务:")
        # elif type(self.testSet[0][-1]) is float or type(self.testSet[0][-1]) is int:#若为实数型，即为回归任务
        #     print("回归任务:")
        #     regression  = True
        regression = False
        print("回归任务:")
#      求得所有测试集的结果列表
        results = [self.classifyLabel(self.testSet[i],regression) for i in range(len(self.testSet))]
        if regression:
            for i in range(len(self.testSet)):
                print("测试",i+1,self.testSet[i][-1],"测试结果:",results[i], "相对误差:",
                      (self.testSet[i][-1] - results[i]) / self.testSet[i][-1])
        else:
            for i in range(len(self.testSet)):
                print("测试",i+1,self.testSet[i][-1],"测试结果:",results[i],
                      "判断结果:",self.testSet[i][-1] == results[i])

if __name__ == "__main__":
    exp = KNN("/home/ubuntu/PycharmProjects/KNN/venv/data/seeds.csv",k = 5)
    exp.test("seeds")

