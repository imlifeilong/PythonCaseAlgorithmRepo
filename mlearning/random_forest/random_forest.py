from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

import numpy as np
from scipy.special import comb

'''
随机森林
    是一种集成算法，在数据上建立多个模型，并集成所有模型的结果，汇总之后得到一个综合的结果。
    多个模型集成的模型叫集成评估器，中间的每个模型叫做基评估器，一般有三种：装袋法(Bagging)，提升法(Boosting)，堆叠法(Stacking),
    随机森林采用的就是装袋法，它的所有基评估器都是决策树
随机森林分类器 分类树组成
随机森林回归器 回归树组成
'''

wine = load_wine()

# 分割测试集，训练集
xtrain, xtest, ytrain, ytest = train_test_split(wine.data, wine.target, test_size=0.3)
# 决策树分类
clf = DecisionTreeClassifier(random_state=0)
# 随机森林分类
rfc = RandomForestClassifier(random_state=0)

# 训练
clf.fit(xtrain, ytrain)
rfc.fit(xtrain, ytrain)

# 测试
score_c = clf.score(xtest, ytest)
score_r = rfc.score(xtest, ytest)

print(f'Tree:{score_c}', f'Forest:{score_r}')

# 交叉验证对比决策树和随机森林
# n_estimators 随机森林评估器数量，越大效果越好，需要的计算量和内存也大训练时间会变长
rfc = RandomForestClassifier(n_estimators=25)
rfcs = cross_val_score(rfc, wine.data, wine.target, cv=20)

cld = DecisionTreeClassifier()
clfs = cross_val_score(clf, wine.data, wine.target, cv=20)

plt.plot(range(1, 21), rfcs, label='random forest')
plt.plot(range(1, 21), clfs, label='decision tree')
plt.legend()
plt.show()

rfc_res, clf_res = [], []
# 执行10次交叉验证，每次验证20次，并取平均值
for i in range(10):
    rfc = RandomForestClassifier(n_estimators=25)
    rfcs = cross_val_score(rfc, wine.data, wine.target, cv=20).mean()

    clf = DecisionTreeClassifier()
    clfs = cross_val_score(clf, wine.data, wine.target, cv=20).mean()
    rfc_res.append(rfcs)
    clf_res.append(clfs)

plt.plot(range(1, 11), clf_res, label='decision tree')
plt.plot(range(1, 11), rfc_res, label='random forest')

plt.legend()
plt.show()

# data = []
# for i in range(100):
#     rfc = RandomForestClassifier(n_estimators=i + 1, n_jobs=-1)
#     rfcs = cross_val_score(rfc, wine.data, wine.target, cv=10).mean()
#     data.append(rfcs)
#
# print(max(data), data.index(max(data)))
#
# plt.figure(figsize=[20, 5])
# plt.plot(range(1, 101), data)
#
# plt.show()

res = np.array([comb(25, i) * (0.2 ** i) * ((1 - 0.2) ** (25 - i)) for i in range(13, 26)]).sum()
print(res)

# 查看随机森林中每个树的属性
rfc = RandomForestClassifier(n_estimators=10, random_state=2)
rfc.fit(xtrain, ytrain)

rs = rfc.estimators_[0].random_state
print(rs)

for i in range(len(rfc.estimators_)):
    print(rfc.estimators_[i].random_state)

# boostrap 默认是True有放回抽样， 不一定会抽到所有样本，未被抽取的样本叫做 袋外样本
# oob_score 使用袋外模型 不需要划分训练集和测试集
#
rfc = RandomForestClassifier(n_estimators=25, oob_score=True)
rfc.fit(wine.data, wine.target)
print(rfc.oob_score_)

rfc = RandomForestClassifier(n_estimators=25)
rfc.fit(xtrain, ytrain)

rfc.score(xtest, ytest)

# 返回对应分类的概率
rs = rfc.predict_proba(xtest)
print((rs))
