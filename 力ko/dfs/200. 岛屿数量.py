class Solution:
    def numIslands(self, grid):
        def dfs(i, j):
            grid[i][j] = '2'  # 将遍历过的岛置为2

            # 试探 上下左右 四个方向
            for x0, y0 in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x, y = x0 + i, y0 + j
                # 这四个点 不越界，并且值为1的时候，再递归的去试探它的四个方向
                if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                    dfs(x, y)

        m = len(grid)
        n = len(grid[0])

        # 0 表示海洋
        # 1 表示陆地（未访问过）
        # 2 表示陆地（已经访问过）
        count = 0
        for i in range(m):
            for j in range(n):
                # 找到值为1的 然后找到与它相连的所有值为1的格子
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1

        return count


if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    # grid = [
    #     ["1", "1", "0", "0", "0"],
    #     ["1", "1", "0", "0", "0"],
    #     ["0", "0", "1", "0", "0"],
    #     ["0", "0", "0", "1", "1"]
    # ]
    s = Solution()
    res = s.numIslands(grid)
    print(res)
