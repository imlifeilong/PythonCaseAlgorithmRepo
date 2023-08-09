"""
6,3,1,6
3
找到两个相同的数，索引差绝对值小于等于3，输出两个数种最小的那个的索引
"""


def main(data, t):
    res = {}
    for i in range(len(data)):
        if data[i] in data[i + 1:]:
            res[data[i]] = (i, abs(data.index(data[i], i + 1) - i))

    values = sorted(res.values(), key=lambda x: x[1])
    if values and values[0][1] <= t:
        print(values[0][0])
    else:
        print(-1)


s = '6,3,1,6'.split(',')
t = 3

# s = '5,6,7,5,6,7'.split(',')
# t = 2

main(s, t)
