import pandas as pd
from sklearn import tree
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

'''
决策树
    是非参数的有监督学习，从一系列有特征和标签的数据中总结出决策规则，并用树状图的结构呈现这些规则，以解决分类和回归问题

'''



# 加载红酒数据
wine = load_wine()
# 数据形状
print(wine.data.shape)

# 标签矩阵
print(wine.target)

# 将数据和标签合并到一起， axis=1表示按行合并，默认按列
data = pd.concat([pd.DataFrame(wine.data), pd.DataFrame(wine.target)], axis=1)
# print(data)

# 特征名称
print(wine.feature_names)

# 类别名称
print(wine.target_names)
feature_names = ['酒精', '苹果酸', '灰', '灰的碱性', '镁', '总酚', '类黄酮', '非黄烷类酚类', '花青素', '颜色强度', '色调', 'od280/od315稀释葡萄酒', '脯氨酸']

# 分割测试集，训练集
xtrain, xtest, ytrain, ytest = train_test_split(wine.data, wine.target, test_size=0.3)

# criterion 分裂节点时评判准则 gini 基尼系数、entropy 信息增益
# random_state 设置分支随机性，高纬度的数据集中效果比较明显
# splitter 控制决策树中随机选项 best 随机的时候会更倚重于权重高的特征， random 随机选择不会因为权重 可以防止过拟合
# best 选择权重高的特征，
# random 随机选择，防止过拟合
clf = tree.DecisionTreeClassifier(
    criterion='entropy',
    random_state=2,
    splitter='random',
    # max_depth=3,  # 限定树的层数，特征多，训练集少的情况，可以限制层数
    # min_samples_leaf=10,  # 一个节点分支后，每个子节点必须至少20个样本，否则就不会分支，太小会过拟合
    # min_samples_split=5,  # 一个节点至少10个样本
    # max_features=5,  # 限制特征数量
    # min_impurity_decrease=0.1,  # 限制信息增益，如果信息增益小于0.1不会产生分支
    # class_weight=0.2,  # 对样本标签进行均衡，给少量的标签更多的权重，不设置会自动调节
    # min_weight_fraction_leaf=5,  # 基于权重来剪枝
)
# 训练
clf = clf.fit(xtrain, ytrain)
# 测试
score = clf.score(xtest, ytest)
print(score)

# 返回测试样本所在叶子节点的索引
apply = clf.apply(xtest)
print(apply)
# 返回测试样本预测结果
pre_data = clf.predict(xtest)
print(pre_data)

import graphviz

dot_data = tree.export_graphviz(
    clf,
    feature_names=feature_names,
    class_names=['maotai', 'xifeng', 'wuliangye'],
    filled=True,  # 添加颜色
    rounded=True  # 框的形状
)
grap = graphviz.Source(dot_data)
# print(grap)

# grap.render('output/wine_tree.gv', view=True)
# 特征的权重.
print(clf.feature_importances_)
mapping = [*zip(feature_names, clf.feature_importances_)]
print(mapping)

score = clf.score(xtrain, ytrain)

print(score)

# 测试层数和分数的曲线
# test = []
# for i in range(10):
#     clf = tree.DecisionTreeClassifier(
#         max_depth=i + 1,
#         criterion="entropy",
#         random_state=30,
#         splitter="random"
#     )
#     clf = clf.fit(xtrain, ytrain)
#     score = clf.score(xtest, ytest)
#     test.append(score)
# plt.plot(range(1, 11), test, color="red", label="max_depth")
# plt.legend()
# plt.show()
