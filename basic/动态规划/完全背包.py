"""
有 n 个物品和一个承重为 m 的背包. 给定数组 W表示每个物品的重量和数组 V 表示每个物品的价值。问最多能装入背包的总价值是多大?

例如：

n=5, m = 10, W = [2, 2, 6, 5, 4], V = [6, 3, 5, 4, 6]

物品数量无限制
"""


class Solution:
    def tbag(self, n, m, w, v):
        """

        :param n: 物品个数
        :param m: 背包能装的最大重量
        :param w: 数组中存放每个物品的重量
        :param v: 数组中存放每个物品的价值
        :return:
        """
        self.n = n
        self.w = w
        self.v = v
        self.m = m
        self.length = len(self.v)
        res = self.process(0, self.m)
        print(res)
        res1 = self.process_dp()
        print(res1)

    def process(self, index, m):
        '''
        :param index:
        :param m:
        :return:
        '''
        if index == self.length or m == 0:
            return 0
        # 当前货物重量超过背包容量，去装下一个位置
        if w[index] > m:
            return self.process(index + 1, m)
        # 可以装当前货物，但是不装，去下个位置装
        p1 = self.process(index + 1, m)
        # 可以装当前货物，装上后，继续装当前货物（所有货物数量无限制）
        p2 = self.process(index, m - w[index]) + v[index]
        return max(p1, p2)

    def process_dp(self):
        dp = [[0] * (self.m + 1) for _ in range(self.n + 1)]

        for i in range(self.n - 1, -1, -1):
            for j in range(1, self.m + 1):
                # 当前货物的重量大于背包容量
                if self.w[i] > j:
                    dp[i][j] = dp[i + 1][j]
                else:
                    p1 = dp[i + 1][j]
                    p2 = dp[i][j - self.w[i]] + self.v[i]
                    dp[i][j] = max(p1, p2)

        for row in dp:
            print(row)

        print(dp[0][self.m])
        return dp[0][self.m]


if __name__ == '__main__':
    s = Solution()
    n = 5
    m = 10
    w = [1, 4, 6, 5, 4]
    v = [6, 7, 5, 4, 6]
    s.tbag(n, m, w, v)
