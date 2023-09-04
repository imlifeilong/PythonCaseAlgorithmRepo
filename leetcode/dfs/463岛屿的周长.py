class Solution:
    def islandPerimeter(self, grid):
        def dfs(i, j):

            # 遇见左右边界的情况 都可以算做上一个点的边长
            if i < 0 or i >= m:
                return 1
            # 遇到上下边界的情况，可以算做上一个点的边长
            if j < 0 or j >= n:
                return 1
            # 遇见水的情况 可以算做上一个点的边长
            if grid[i][j] == 0:
                return 1
            # 遇见已经访问的陆地，相邻的，不能算边长
            if grid[i][j] == 2:
                return 0

            grid[i][j] = 2  # 将遍历过的岛置为2
            # 统计该点四周的情况
            tmp = 0
            # 试探 上下左右 四个方向
            for x0, y0 in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x, y = x0 + i, y0 + j
                # 不用判断是否越界，遇到边界可以算作边长，将得到的边长累加
                tmp += dfs(x, y)

            return tmp

        m = len(grid)
        n = len(grid[0])

        # 0 表示海洋
        # 1 表示陆地（未访问过）
        # 2 表示陆地（已经访问过）

        p = 0
        for i in range(m):
            for j in range(n):
                # 找到岛屿的起始位置，然后找到所有相连的岛 面积
                if grid[i][j] == 1:
                    p = dfs(i, j)
                    break

        return p


if __name__ == '__main__':
    grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    s = Solution()
    res = s.islandPerimeter(grid)
    print(res)
