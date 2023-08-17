# 695. 岛屿的最大面积
def main(data):
    def dfs(i, j):
        # i 和 j 在边界范围内，并且当前有矿
        if 0 <= i < m and 0 <= j < n and data[i][j]:
            # 为了确保每个土地访问不超过一次，我们每次经过一块土地时，将这块土地的值置为0
            area = data[i][j]
            data[i][j] = 0

            # 当前矿的值加上四周的值，
            # i-1, j 上
            # i+1, j 下
            # i, j-1 左
            # i, j+1 右
            return area + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)
        return 0

    # m 行数 n 列数
    m, n = len(data), len(data[0])
    res = 0
    for i in range(m):
        for j in range(n):
            if data[i][j]:
                res = max(res, dfs(i, j))
    print(res)


s = '''22220
00000
00000
01111'''.split('\n')


s = '''22220
00020
00010
01111'''.split('\n')
s = '''20000
00020
00000
00111'''.split('\n')
data = list(map(lambda x: [int(i) for i in x], s))
print(data)
main(data)
