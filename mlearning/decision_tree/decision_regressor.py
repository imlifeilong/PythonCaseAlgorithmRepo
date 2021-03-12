import random
import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.model_selection import cross_val_predict
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# 加载波士顿房价数据
boston = load_boston()
# 数据形状
print(boston.data.shape)

# 标签矩阵
print(boston.target)

# 将数据和标签合并到一起， axis=1表示按行合并，默认按列
data = pd.concat([pd.DataFrame(boston.data), pd.DataFrame(boston.target)], axis=1)
print(data)

# 特征名称
print(boston.feature_names)

regressor = tree.DecisionTreeRegressor(random_state=0)
cross_val_predict(regressor, boston.data, boston.target, cv=10)

rng = np.random.RandomState(1)  # 随机数种子
# rng.rand(80, 1) 80行1列的二维数组，训练时不能使用1维的
# 生成0-5之间的随机数
X = np.sort(5 * rng.rand(80, 1), axis=0)
# 生成正弦函数，ravel() 将结果转换成1维的
y = np.sin(X).ravel()
# 给结果加点噪音，
y[::5] += 3 * (0.5 - rng.rand(16))

# 建立模型
reg_1 = tree.DecisionTreeRegressor(max_depth=4)
reg_2 = tree.DecisionTreeRegressor(max_depth=9)

# 开始训练
reg_1.fit(X, y)
reg_2.fit(X, y)

# 产生测试集在0到5之间，步长为0.01
# np.newaxis增加维度，将数据变成2维
xtest = np.arange(0.0, 5, 0.01)[:, np.newaxis]
print(xtest)

y1 = reg_1.predict(xtest)
y2 = reg_2.predict(xtest)

print(y1)
print(y2)

#  打开一块画布
plt.figure()
# 散点图
# edgecolors 点变的颜色
# s 点大小
plt.scatter(X, y, s=20, edgecolors='black', c='darkorange', label='data')
# 折线图
plt.plot(xtest, y1, color='blue', label='max_depth=2', linewidth=2)
plt.plot(xtest, y2, color='green', label='max_depth=5', linewidth=2)
plt.xlabel('data')
plt.ylabel('target')

plt.title('huiguishu')
# 显示图例
plt.legend()
plt.show()
