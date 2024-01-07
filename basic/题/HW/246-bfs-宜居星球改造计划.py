def main(data):
    m = len(data)
    n = len(data[0])

    """
    思路
    1、先获取所有NO个数
    2、获取YES的坐标
    3、开始改造，每个YES坐标的 上 下 左 右，每改造1次记录+1
    4、直到所有的NO改造完成，或者......
    """
    no_count = 0  # 记录NO的个数
    yes_points = []  # 记录YES的坐标
    for i in range(m):
        for j in range(n):
            if data[i][j] == 'NO':
                no_count += 1
            if data[i][j] == 'YES':
                yes_points.append((i, j))

    day_count = 0  # 记录天数

    # 当NO的数据为0，并且没有可以扩展的YES时 退出循环
    while no_count > 0 and yes_points:

        tmp_points = []

        # 遍历所有的YES坐标，
        for i, j in yes_points:
            # 分别 试探 当前点的 上 下 左 右 能否改造
            for x0, y0 in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x, y = x0 + i, y0 + j

                # 如果有一个方向不能改造（到边界，或者是NA），就跳过
                if not (0 <= x < m and 0 <= y < n) or data[x][y] in ('YES', 'NA'):
                    continue

                # 改造过的标记一下
                data[x][y] = 'YES'

                # 打印看下改造过程
                for row in data:
                    print(row)

                # 记录改造过的YES，然后继续进行这些点上下左右的改造
                tmp_points.append((x, y))
                # 当前点改造过后，NO的个数减1
                no_count -= 1

        yes_points = tmp_points

        # 每改造一次天数加1
        day_count += 1

    if no_count > 0:
        print(-1)
    else:
        print(day_count)


s = """YES YES NO
NO NO NO
YES NO NO""".split('\n')

s = """YES NO NO NO
NO NO NO NO
NO NO NO NO
NO NO NO NO""".split('\n')
s = """YES NO NO YES
NO NO YES NO
NO YES NA NA
YES NO NA NO""".split('\n')
data = list(map(lambda x: x.split(), s))
main(data)
