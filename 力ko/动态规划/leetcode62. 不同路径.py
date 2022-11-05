'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？
'''


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = self.process(0, 0, m, n)
        print(res)

    def process(self, i, j, m, n):
        # 当走到最下边，刚好走到最右边了
        if i == m - 1 and j == n - 1:
            return 1
        # 如果走到最左边，或者走到最下边 并没有走到终点
        if i == m or j == n:
            return 0

        return self.process(i + 1, j, m, n) + self.process(i, j + 1, m, n)


if __name__ == '__main__':
    s = Solution()
    s.uniquePaths(3, 7)
