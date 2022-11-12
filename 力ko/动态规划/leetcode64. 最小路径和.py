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


if __name__ == '__main__':
    s = Solution()
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    grid = [[1, 2, 3], [4, 5, 6]]
    s.minPathSum(grid)
