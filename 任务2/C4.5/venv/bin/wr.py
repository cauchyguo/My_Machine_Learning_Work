from  math import *
import csv
from collections import Counter
from random import *

class C45:
    def __init__(self,filename):
        self.dataset = [] #数据集
        self.file_reader(file_name=filename)
        self.myTree = None

    def file_reader(self,file_name):#读取文件提取数据集
        self.dataset = [] #数据集dadaset
        with open(file_name, newline='') as csvfile:
            line = csvfile.readline()
            Line = [x for x in line.split(',')]
            self.Line = Line[:-1]
            data = csv.reader(csvfile)
            for line in data:
                row = [x.strip() for x in line]
                # a = row[0]
                # row[0] = row[-1]
                # row[-1] = a
                if row != [] and row != [""] and '?' not in row:
                    self.dataset.append(row)
        # print(self.dataset)

    def calcShannonEnt(self,dataset):
        """计算当前样本集合的信息熵"""
        numSam = len(dataset)  # 统计样本的数量
        labelCounts = {}  # 创建一个字典存储样本的的分类机器对应的数量
        for sample in dataset:
            currentLabel = sample[-1]  # 数据集中通常最后一位为标签属性
            if currentLabel not in labelCounts.keys():  # 将不存在的类别添字典置为0
                labelCounts[currentLabel] = 0
            labelCounts[currentLabel] += 1 #统计在当前样本集中各个类的种数
        shannonEnt = 0.0
        for key in labelCounts:
            prob = float(labelCounts[key]) / numSam #统计该类所占百分比
            shannonEnt -= prob * log(prob, 2)
        return round(shannonEnt,4)

    def splitDataSet(self,dataset,axis,value):
        """提取样本集某属性为特定值的样本"""
        restDataSet = []
        for sample in dataset:
            sam1 = []
            if sample[axis] == value:
                sam1 = sample[:]
                sam1.pop(axis)
                restDataSet.append(sam1)
        return restDataSet #返回数据集某个属性为特定值value的数据集

    def chooseBestAttr(self,dataset):
        """选择最好的数据集划分属性,并返回该属性的下标"""
        baseEnt = self.calcShannonEnt(dataset) #样本划分前的信息熵
        bestGain = 0.0
        bestAttrIdx = 0  #最佳划分属性默认为第一个属性
        for i in range(len(dataset[0])-1): #对样本中的非标签属性一一进行判别,取最大信息增益的属性
            attrsList = [sample[i] for sample in dataset]
            uniqueAttrsL = set(attrsList) #得到属性的所有属性值域
            newEnt = 0.0
            splitInf = 0.0
            for value in uniqueAttrsL:
                subDataSet = self.splitDataSet(dataset,i,value) #将样本集按照属性下不同的取值进行圈划
                prob = len(subDataSet)/(float)(len(dataset)) #对统计新划得的集合的信息（信息熵
                newEnt += prob*self.calcShannonEnt(subDataSet) #按照所占权重统计划分后的信息熵）
                splitInf -= prob*log(prob,2) #属性value的固有值
            infoGain = (baseEnt - newEnt) /  splitInf #求得当下划分属性的增益熵/固有值
            if(infoGain > bestGain): #选出增益率最大的划分属性
                bestGain = infoGain
                bestAttrIdx = i #并标记该属性对应样本的下标索引
        return bestAttrIdx

    def majorLabel(self,classList):
        """函数用于统计某个样本集下类别数最多的类别"""
        statistical = Counter(classList) #使用Counter类来统计比例最高的类
        majorLabel = statistical.most_common(1)
        return majorLabel[0][0]

    def creatTree(self,dataset,labels,selectAttrbutes):
        """创建决策树"""
        attrs = labels[:]
        # classList = [sample[-1] for sample in dataset]
        classList = []
        for sample in dataset:
            classList.append(sample[-1])
        if classList.count(classList[0]) == len(classList):
            return  classList[0] #当所有样本标签相同时结束迭代，返回标签
        if (len(dataset[0]) == 1): #若划分的节点的属性为零即数据集只有标签值
            return self.majorLabel(classList)  #返回当前节点样本集中占据多数的标签（类）

        bestAttrIdx = self.chooseBestAttr(dataset) #选出当前节点的最佳划分属性并返回下标
        bestAttrLabel = attrs[bestAttrIdx] #由labels列表提取对应划分属性的名称（储存为节点数据）

        #存储节点的层数
        length = len(self.labels) -len(attrs) + 1
        #建立字典存储每层的属性
        if length not in selectAttrbutes.keys():
            selectAttrbutes[length] = []
        selectAttrbutes[length].append(bestAttrLabel)

        myTree = {bestAttrLabel:{}} #以最佳分类属性为节点建立一个空树{}为字典{}内储存节点信息（节点的测试属性和节点下的样本集）
        del (attrs[bestAttrIdx]) #从labels列表中删除已经被选出来当节点的属性
        attrValues = [sample[bestAttrIdx] for sample in dataset]
        uniqueVals = set(attrValues) #找出该属性所有不重复的属性值
        myTree[bestAttrLabel]['majorLabel'] = self.majorLabel(classList) #键majorLabel表示该节点下占最多的类
        for value in uniqueVals:
            subLabels = attrs[:] #切边
            myTree[bestAttrLabel][value] = self.creatTree\
                    (self.splitDataSet(dataset,bestAttrIdx,value),subLabels,selectAttrbutes)
        self.myTree = myTree
        return myTree,selectAttrbutes

    def classify(self,inputTree,attrs,testSample):
        """根据决策树对传递过来的样本进行决策"""
        test = False #test用作是否能在决策树下找到所有的属性值
        _a = list(inputTree.keys())
        firstAttr = _a[0] #得到决策树第一个节点的测试属性

        splitSet = inputTree[firstAttr] #该测试属性下的字典样本集
        AttrIdx = attrs.index(firstAttr)
        for key in splitSet.keys(): #key 为firstAttr属性下的一个唯一取值
            if str(testSample[AttrIdx]) == key: #若样本firAttr属性值存在于决策树下
                test = True
                if type(splitSet[key]).__name__ == 'dict': #为字典表明在该属性下还有其他属性的子树划分
                    samLabel = self.classify(splitSet[key], attrs, testSample) #继续迭代
                else:
                    samLabel = splitSet[key] #表明触底为叶节点,直接得到分类名
        if not test:
            samLabel = splitSet['majorLabel'] #若在当前属性节点下无对应的属性值匹配样本，则返回该节点下最多的类名

        return samLabel

    def a_train(self,labels):
        """一次测试"""
        testSet = []  #测试集
        trainSet = [] #训练集
        numTestSet = int(len(self.dataset) / 3) #测试集占样本总数的1/3
        for i in range(numTestSet):
            x = randint(0,len(self.dataset) - 1) #每次从样本集中随机取样
            testSet.append(self.dataset[x])
        for sample in self.dataset: #将不出现在测试集中的所有样本添加至训练集中,即测试集与训练集无交集
            if sample not in testSet:
                trainSet.append(sample)
        selectAttrs = {}
        mytree,selectAttrs = self.creatTree(trainSet,labels,selectAttrs)
        count = 0 #统计分类正确率
        for testVc in testSet:
            if self.classify(mytree,self.labels,testVc) == testVc[-1]:
                count += 1
        print("挑选的特征属性为：",selectAttrs)
        print("训练集数目",len(trainSet),"测试集数目",len(testSet),"正确率",'{:.2%}'.format(count/numTestSet))

    def train_for_n_times(self,datasetname,labels,n):
        '''进行n次测试'''
        self.labels = labels[:]
        print("数据集：", datasetname,"样本属性数量：",len(self.labels),"样本总数:",len(self.dataset),"评估方法:","自助法")
        for i in range(n):
            self.labels = labels[:]
            print("测试",i+1,'',end='')
            self.a_train(self.labels)

if __name__ == '__main__':
    cTree = C45(r'E:\技术报告\任务二\C4.5\venv\Data\car.csv')
    labels = ['buying','maint', 'doors', 'peasons','lug_boot','safety']
    cTree.train_for_n_times("Car", labels, n=12)