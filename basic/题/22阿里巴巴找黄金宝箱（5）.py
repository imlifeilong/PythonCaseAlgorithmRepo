"""
连续k个数的最大值
"""


def main(data, t):
    res = []
    length = len(data)
    for i in range(length - t + 1):
        res.append(sum(data[i:i + 4]))
    res.sort()
    print(res[-1])


s = '2,10,-3,-8,40,5'.split(',')
data = list(map(int, s))
t = 4
s = '8'.split(',')
data = list(map(int, s))
t = 1
main(data, t)
