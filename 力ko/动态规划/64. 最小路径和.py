'''
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。
'''
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        res = self.process(0, 0, len(grid), len(grid[0]), grid)
        print(res)
        x, y = len(grid), len(grid[0])
        res1 = self.process2(x - 1, y - 1, grid)
        print(res1)
        cache = [[None] * (y) for _ in range(x)]

        res2 = self.process_cache(x - 1, y - 1, grid, cache)
        print(res2)
        self.process_dp(x, y, grid)

    def process(self, i, j, x, y, a):
        """
        :param i:
        :param j:
        :param x:
        :param y:
        :param a:
        :return:
        """
        # 到达最后一个单元格
        if i == x - 1 and j == y - 1:
            return a[i][j]
        # 最右列 只能向下
        if i == x - 1:
            return self.process(i, j + 1, x, y, a) + a[i][j]
        # 最下行 只能向右
        if j == y - 1:
            return self.process(i + 1, j, x, y, a) + a[i][j]
        return min(self.process(i + 1, j, x, y, a), self.process(i, j + 1, x, y, a)) + a[i][j]

    def process2(self, x, y, a):
        if x == 0 and y == 0:
            return a[x][y]
        if x == 0:
            return self.process2(x, y - 1, a) + a[x][y]
        if y == 0:
            return self.process2(x - 1, y, a) + a[x][y]
        return min(self.process2(x - 1, y, a), self.process2(x, y - 1, a)) + a[x][y]

    def process_cache(self, x, y, a, cache):
        if cache[x][y]:
            return cache[x][y]
        if x == 0 and y == 0:
            cache[x][y] = a[x][y]
        elif x == 0:
            cache[x][y] = self.process_cache(x, y - 1, a, cache) + a[x][y]
        elif y == 0:
            cache[x][y] = self.process_cache(x - 1, y, a, cache) + a[x][y]
        else:
            cache[x][y] = min(self.process_cache(x - 1, y, a, cache), self.process_cache(x, y - 1, a, cache)) + a[x][y]
        return cache[x][y]

    def process_dp(self, x, y, a):
        dp = [[None] * (y) for _ in range(x)]

        for i in range(x):
            for j in range(y):
                if i == 0 and j == 0:
                    dp[i][j] = a[i][j]
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] + a[i][j]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + a[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + a[i][j]

        print(dp[x - 1][y - 1])


if __name__ == '__main__':
    s = Solution()
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    grid = [[1, 2, 3], [4, 5, 6]]
    s.minPathSum(grid)
