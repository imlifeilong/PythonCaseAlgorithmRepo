def main(m, n, data):
    def dfs(i, j, end):
        # i j 是否是终点 能否走到 end的点

        # 当到达终点时返回
        if 0 <= i < m and 0 <= j < n and (i, j) == end:
            return True

        # 分别 试探 当前点的 上 下 左 右
        for x0, y0 in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x, y = x0 + i, y0 + j

            # 如果右一个方向走不通（到边界，或者有障碍），就跳过
            if not (0 <= x < m and 0 <= y < n) or data[x][y] == '1':
                continue

            # 走过的位置 改为 1
            data[i][j] = '1'

            res = dfs(x, y, end)
            # 记录后再还原
            data[i][j] = '0'

            # 如果当前的到四个方向 有一种可以走到终点就返回正确
            if res:
                return True

        return False

    starts = []
    ends = []

    for i in range(m):
        for j in range(n):
            # 将3的点记为结束点
            if data[i][j] == '3':
                ends.append((i, j))
            # 将2的点记为开始点
            elif data[i][j] == '2':
                starts.append((i, j))

    count = 0

    for j in ends:
        # 试探两人都能到达 终点
        res = True
        for i in starts:
            res &= dfs(*i, j)
        if res:
            count += 1
    print(count)


s = """2 1 0 3
0 1 2 1
0 3 0 0
0 0 0 0""".split('\n')
# s = """2 1 2 3
# 0 1 0 0
# 0 1 0 0
# 0 1 0 0""".split('\n')
data = list(map(lambda x: x.split(), s))
print(data)
m = 4
n = 4
main(m, n, data)
