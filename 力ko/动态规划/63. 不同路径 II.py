'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 1 和 0 来表示。

'''
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        res = self.process(0, 0, len(obstacleGrid), len(obstacleGrid[0]), obstacleGrid)
        print('res', res)

        res1 = self.process_1(0, 0, len(obstacleGrid), len(obstacleGrid[0]), obstacleGrid)
        print('res1', res1)
        res2 = self.process2(len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1, obstacleGrid)
        print('res2', res2)
        x, y = len(obstacleGrid), len(obstacleGrid[0])
        cache = [[None] * (x + 1) for _ in range(y + 1)]
        res3 = self.process_cache(x - 1, y - 1, obstacleGrid, cache)
        print('res3', res3)
        self.process_dp(x, y, obstacleGrid)

    def process(self, i, j, x, y, a):
        if i == x or j == y or a[i][j] == 1:
            return 0
        if i == x - 1 and j == y - 1:
            return 1
        return self.process(i + 1, j, x, y, a) + self.process(i, j + 1, x, y, a)

    def process_1(self, i, j, x, y, a):
        if i == x or j == y:
            return 0
        if a[i][j] != 1:
            if i == x - 1 and j == y - 1:
                return 1
            return self.process_1(i + 1, j, x, y, a) + self.process_1(i, j + 1, x, y, a)
        return 0

    def process2(self, x, y, a):
        if a[x][y] ==1:
            return 0
        if x == 0 or y == 0:
            return 1
        return self.process2(x - 1, y, a) + self.process2(x, y - 1, a)

    def process_cache(self, x, y, a, cache):
        if cache[x][y]:
            return cache[x][y]
        if a[x][y] == 1:
            cache[x][y] = 0
        elif x == 0 or y == 0:
            cache[x][y] = 1
        else:
            cache[x][y] = self.process_cache(x - 1, y, a, cache) + self.process_cache(x, y - 1, a, cache)
        return cache[x][y]

    def process_dp(self, x, y, a):
        dp = [[None] * (x) for _ in range(y)]

        for i in range(x):
            for j in range(y):
                if a[i][j] == 1:
                    dp[i][j] = 0
                elif i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        print(dp[x - 1][y - 1])


if __name__ == '__main__':
    s = Solution()
    obstacleGrid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    obstacleGrid = [[0, 1], [0, 0]]
    # obstacleGrid = [[0, 1], [0, 0]]
    s.uniquePathsWithObstacles(obstacleGrid)
