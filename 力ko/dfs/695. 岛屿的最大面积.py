class Solution:
    def maxAreaOfIsland(self, grid):
        def dfs(i, j):
            # 遍历过的岛屿记录为2
            grid[i][j] = 2
            tmp = 1

            # 试探 上下左右 四个方向

            for x0, y0 in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x, y = x0 + i, y0 + j
                # 这四个点 不越界，并且值为1的时候，再递归的去试探它的四个方向
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    # 将所有相连的面积加在一起
                    tmp += dfs(x, y)
            # 返回面积
            return tmp

        m = len(grid)
        n = len(grid[0])

        # 0 表示海洋
        # 1 表示陆地（未访问过）
        # 2 表示陆地（已经访问过）

        area = 0
        for i in range(m):
            for j in range(n):
                # 找到岛屿的起始位置，然后找到所有相连的岛 面积
                if grid[i][j] == 1:
                    area = max(area, dfs(i, j))

        return area


if __name__ == '__main__':
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    s = Solution()
    res = s.maxAreaOfIsland(grid)
    print(res)
