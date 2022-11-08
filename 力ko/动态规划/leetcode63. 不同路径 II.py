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
        print(res)

        res1 = self.process_1(0, 0, len(obstacleGrid), len(obstacleGrid[0]), obstacleGrid)
        print(res1)

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


if __name__ == '__main__':
    s = Solution()
    obstacleGrid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    # obstacleGrid = [[0, 1], [0, 0]]
    s.uniquePathsWithObstacles(obstacleGrid)
