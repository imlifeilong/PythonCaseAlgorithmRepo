def main(data, e):
    length = len(data)
    points = []
    x, y = 0, 0
    # 找到所有点的坐标
    for i in range(1, e):
        if i <= length:
            points.append([i - 1, data[i - 1][1] + y])
            y = data[i - 1][1] + y
        else:
            points.append([i - 1, y])

    # 两点之间的横坐标差值为1，所以面积就是纵坐标的值
    area = 0
    for p in points:
        area += p[1]
    print(area)


def get_area(data, e):
    x0, y0 = 0, 0
    area = 0
    for i in range(len(data)):
        x = data[i][0]
        y = data[i][1]
        area += (x - x0) * abs(y0)
        x0 = x
        y0 += y  # y轴进行偏移
    if x0 < e:
        area += (e - x0) * abs(y0)
    print(area)


def parse(data):
    return [int(x) for x in data.split()]


n = 4
e = 10
s = """1 1
2 1
3 1
4 -2"""

data = list(map(parse, s.split('\n')))
print(data)
# main(data, e)
get_area(data, e)
