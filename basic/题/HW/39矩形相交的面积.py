def main(data):
    """
    思路 通过画图可以知道，几个矩形相交的地方
    长是矩形们 左边界的最大值 与 右边界的最小值 的差值
    宽是矩形们 上边界的最大值 与 下边界的最小值 的差值
    :param data:
    :return:
    """
    x1, y1, w1, h1 = data[0]
    x2, y2, w2, h2 = data[1]
    x3, y3, w3, h3 = data[2]
    w = min(x1 + w1, x2 + w2, x3 + w3) - max(x1, x2, x3)
    h = min(y1, y2, y3) - max(y1 - h1, y2 - h2, y3 - h3)
    print(w * h)


s = """1 6 4 4
3 5 3 4
0 3 7 3""".split('\n')

data = list(map(lambda x: [int(i) for i in x.split()], s))
# print(data)
main(data)
