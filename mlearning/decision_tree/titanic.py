import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score

data = pd.read_csv('data/titanic/train.csv')

# 数据信息，数据列，数据类型，每列有多少数据
data.info()

print(data.head())
print(data.columns)

# 删除一些对数据影响不大的特征
# inplace=True 表示在原始数据上进行操作，默认在副本集
# axis=1 表示对列进行操作
data.drop(['Cabin', 'Name', 'Ticket'], inplace=True, axis=1)
print(data)

# 补充缺失值
# 年龄使用均值填补
data['Age'] = data['Age'].fillna(data['Age'].mean())

# 删除有缺失值的行
data = data.dropna()

# 去重
labels = data['Embarked'].unique().tolist()

# 非数字型转换成数字
data['Embarked'] = data['Embarked'].apply(lambda x: labels.index(x))

# 将性别转换成数字
data['Sex'] = (data.loc[:, 'Sex'] == 'male').astype(int)

print(data.head())

# 取出不是Survived的列
x = data.iloc[:, data.columns != 'Survived']
# 取出Survived的列
y = data.iloc[:, data.columns == 'Survived']

# 分开测试集训练集
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.3)
# print(xtrain)
# 恢复索引，会多出index列
# xtrain.reset_index(inplace=True)
# print(xtrain)

# 恢复索引
for i in [xtrain, xtest, ytrain, ytest]:
    i.index = range(i.shape[0])

clf = DecisionTreeClassifier(random_state=25)

clf = clf.fit(xtrain, ytrain)
score = clf.score(xtest, ytest)

print(score)

clf = DecisionTreeClassifier(random_state=25)
# 交叉验证，执行15次，取平均值
score = cross_val_score(clf, x, y, cv=15).mean()

print(score)

# 调参
tr, te = [], []

for i in range(10):
    clf = DecisionTreeClassifier(
        random_state=25,
        max_depth=i + 1,
        criterion='entropy'
    )
    clf = clf.fit(xtrain, ytrain)
    score_tr = clf.score(xtrain, ytrain)

    score_te = cross_val_score(clf, x, y, cv=10).mean()
    tr.append(score_tr)
    te.append(score_te)

print(max(te))

plt.plot(range(1, 11), tr, color='red', label='train')
plt.plot(range(1, 11), te, color='blue', label='test')

plt.xticks(range(1, 11))
plt.legend()

# plt.show()

# 生成0-0.5之间50个连续的随机数
np.linspace(0, 0.5, 50)

clf = DecisionTreeClassifier(random_state=25)

# 训练参数，算法可以自己选择合适的参数
par = {
    'criterion': ('gini', 'entropy'),
    'splitter': ('best', 'random'),
    'max_depth': [*range(1, 10)],
    'min_samples_leaf': [*range(1, 50, 5)],
    'min_impurity_decrease': [*np.linspace(0, 0.5, 5)]
}

# 网格搜索训练
gs = GridSearchCV(clf, par, cv=10)

gs = gs.fit(xtrain, ytrain)

score = gs.score(xtest, ytest)
print(score)

# 返回最佳参数组合
print(gs.best_params_)

# 返回模型的评判标准
print(gs.best_score_)
