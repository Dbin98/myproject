#!/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/10/29 13:15
# @Author  :db
# @Site    :
# @File    :add.py
# @Software:PyCharm
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.feature_selection import VarianceThreshold
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import jieba
import pandas as pd
def cut_word(text):
    """
    中文分词
    :param text:
    :return:
    """
    return " ".join(list(jieba.cut(text)))

def datesets_demo():
    # 获取数据集
    iris = load_iris()
    print("鸢尾花数据集\n",iris)
    print("鸢尾花数据集描述\n", iris["DESCR"])
    print("查看特征值\n", iris.feature_names)

    #数据集划分
    x_train,x_test,y_train,y_test = train_test_split(iris.data,iris.target,test_size=0.2,random_state=22)
    print("训练集的特征值\n",x_train,x_train.shape)
    return None

def dict_demo():
    """
    字典特征提取
    """
    data=[{'name':'小皮','high':165},{'name':'小邓','high':173},{'name':'等等','high':188}]
    #1、实例化转换器类
    transfer = DictVectorizer(sparse=False)
    #2、调用fit_transform()
    data_new = transfer.fit_transform(data)
    print("data_new\n",data_new)
    print("特征值\n", transfer.get_feature_names())
    return None

def count_chinese_demo():
    """
    文本特征值提取
    """
    data = ["爱国主义，这是一个多么光辉的字眼。古今中外，有多少英雄豪杰，有多少仁人志士，有多少科学伟人，有多少文学巨匠为它而拼搏，为它而奋斗不息！",
            "大家都熟悉南宋抗金名将岳飞，他牢记母训“精忠报国”，带领岳家军，驰骋疆场，威震敌胆，击退敌人的一次次进攻。南宋末年，宋朝江山土崩瓦解之际，文天祥奋起卫国，终因寡不敌众而被俘。他写下了“人生自古谁无死，留取丹心照汗青”的豪迈诗句，表达了他的爱国之情和誓死不屈的决心。",
            "古罗马有一位叫马塞尔的英雄，当祖国遭受敌人的侵略时，他带领人民奋勇杀敌，在战斗中不幸被俘。敌人威胁他如不投降，就把他烧死。面对穷凶极恶的敌人，马塞尔临危不惧。他慷慨陈辞：“为了祖国免遭强盗的蹂躏，我即使葬身火海也在所不辞。”马塞尔的生命被火神吞噬了，可是他的爱国主义精神永远激励着罗马人民努力奋斗。"]
    data_new = []
    for i in data:
        data_new.append(cut_word(i))
    #1、实例化一个转换器
    transfer = CountVectorizer(stop_words=["太阳升"])
    #2、调用fit_transform
    data_final = transfer.fit_transform(data_new)
    print("data_new\n", data_final.toarray())
    print("特征值\n", transfer.get_feature_names())
    return None

def Tfidf_demo():
    """
    用TF-IDF方法进行文本特征抽取
    :return:
    """
    data = ["爱国主义，这是一个多么光辉的字眼。古今中外，有多少英雄豪杰，有多少仁人志士，有多少科学伟人，有多少文学巨匠为它而拼搏，为它而奋斗不息！",
            "大家都熟悉南宋抗金名将岳飞，他牢记母训“精忠报国”，带领岳家军，驰骋疆场，威震敌胆，击退敌人的一次次进攻。南宋末年，宋朝江山土崩瓦解之际，文天祥奋起卫国，终因寡不敌众而被俘。他写下了“人生自古谁无死，留取丹心照汗青”的豪迈诗句，表达了他的爱国之情和誓死不屈的决心。",
            "古罗马有一位叫马塞尔的英雄，当祖国遭受敌人的侵略时，他带领人民奋勇杀敌，在战斗中不幸被俘。敌人威胁他如不投降，就把他烧死。面对穷凶极恶的敌人，马塞尔临危不惧。他慷慨陈辞：“为了祖国免遭强盗的蹂躏，我即使葬身火海也在所不辞。”马塞尔的生命被火神吞噬了，可是他的爱国主义精神永远激励着罗马人民努力奋斗。"]
    data_new = []
    for i in data:
        data_new.append(cut_word(i))
    # 1、实例化一个转换器
    transfer = TfidfVectorizer(stop_words=["一个","一位","一次次","为了","写下","这是","表达","面对","遭受"])
    # 2、调用fit_transform
    data_final = transfer.fit_transform(data_new)
    print("data_new\n", data_final.toarray())
    print("特征值\n", transfer.get_feature_names())
    return None

def minMax_demo():
    """
    归一化
    :return:
    """
    #1、获取数据
    data = pd.read_table("dating.txt")
    data = data.iloc[:, :3]
    print("data: \n",data)
    #实例化一个转化器
    transfer = MinMaxScaler(feature_range=[1,2])
    #调用transfer.fit_transform
    data_new = transfer.fit_transform(data)
    print("data_new:\n",data_new)
    return None

def stand_demo():
    """
    标准化处理
    :return:
    """
    data = pd.read_table("dating.txt")
    data = data.iloc[:, :3]
    transfer = StandardScaler()
    data_new = transfer.fit_transform(data)
    print("data_new:\n",data_new)

def variance_demo():
    """
    低方差过滤：过滤低方差特征
    :return:
    """
    #1、获取数据
    data = pd.read_csv("factor_returns.csv")
    data = data.iloc[:,1:-2]
    print("data:\n",data)
    #2、实例化transfer
    transfer = VarianceThreshold(threshold=10)#threshold:方差阈值
    #3、调用fit_transform
    data_new = transfer.fit_transform(data)
    print("data_new:\n",data_new,data_new.shape)
    # 计算某两个变量之间的相关性系数
    result = pearsonr(data["revenue"],data["total_expense"])
    print("result:\n",result)
    #可视化c与total_expense之间的相关性
    plt.figure(figsize=(20,8),dpi=100)
    plt.scatter(data["revenue"],data["total_expense"])
    plt.show()
    return None

if __name__=="__main__":
    #代码1：sklearn数据集的使用
    #datesets_demo()
    #代码2:字典类型数据特征提取
    #dict_demo()
    #代码3:文本数据特征提取
    #count_chinese_demo()
    #代码4：jieba分词
    #print(cut_word("我爱北京天安门"))
    #代码5：TF-IDF文本特征抽取
    #Tfidf_demo()
    #代码6：归一化
    #minMax_demo()
    #代码7：标准化
    #stand_demo()
    #代码8：低方差选择
    variance_demo()