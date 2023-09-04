'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？
'''


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = self.process(0, 0, m, n)
        print(res)
        res1 = self.process1(m - 1, n - 1)
        print(res1)

        cache = [[None] * (n + 1) for _ in range(m + 1)]
        # for row in cache:
        #     print(row)
        res2 = self.process_cache(m - 1, n - 1, cache)
        print(res2)
        self.process_dp(m, n)

    def process_cache(self, m, n, cache):
        if cache[m][n] is None:
            if m == 0 or n == 0:
                cache[m][n] = 1
            else:
                cache[m][n] = self.process1(m - 1, n) + self.process1(m, n - 1)

        return cache[m][n]

    def process_dp(self, m, n):
        dp = [[None] * (n) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if j == 0 or i == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        print(dp[m-1][n-1])

    def process(self, i, j, m, n):
        # 走到最右只能向下走，走到最下的时候只能向右走
        if i == m - 1 or j == n - 1:
            return 1
        return self.process(i + 1, j, m, n) + self.process(i, j + 1, m, n)

    def process1(self, m, n):
        # 最上行只能从左边过来，最左列只能从上面下来
        if m == 0 or n == 0:
            return 1
        # (i,j)格子可以从(i-1,j)和(i, j-1)格子过来
        return self.process1(m - 1, n) + self.process1(m, n - 1)


if __name__ == '__main__':
    s = Solution()
    s.uniquePaths(3, 7)
