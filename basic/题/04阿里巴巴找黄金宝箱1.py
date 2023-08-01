"""
宝箱左边的数加起来等于右边的数

"""


def start(data):
    for i in range(len(data)):
        # 左边数之和等于右边数之和
        if sum(data[:i]) == sum(data[i + 1:]):
            return i
    return -1


s = '2,5,-1,8,6'
s = '8,9'
data = [int(i) for i in s.split(',')]
res = start(data)
print(res)
