"""
有 n 个物品和一个承重为 m 的背包. 给定数组 W表示每个物品的重量和数组 V 表示每个物品的价值。问最多能装入背包的总价值是多大?

例如：

n=5, m = 10, W = [2, 2, 6, 5, 4], V = [6, 3, 5, 4, 6]

结果为：15
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
        res = self.process(0, m)
        print(res)
        return self.process_dp()

    def process(self, index, m):
        '''
        第index个货物，装进背包后，背包的价值
        :param index: 货物的编号
        :param m: 背包容量
        :return:
        '''
        # 背包承重为0时，不能放东西
        if index == self.n or m == 0:
            return 0
        # 不能装当前货物，当前货物重量大于背包承重时，去下一个位置装货
        if self.w[index] > m:
            return self.process(index + 1, m)
        else:
            # 能装当前货物，但是不装，去下一个位置装
            p1 = self.process(index + 1, m)
            # 能装当前货物，装上后，去下一个位置再装
            p2 = self.process(index + 1, m - self.w[index]) + self.v[index]
            return max(p1, p2)

    def process_dp(self):
        dp = [[0] * (self.m + 1) for _ in range(self.n + 1)]
        # dp[i][j] 表示 前i件物品放入容量为j的背包的最大价值
        # 依赖i+1 所以从下往上填表， 再从左往右

        for i in range(self.n - 1, -1, -1):
            for j in range(1, self.m):
                # 当前货物的重量大于背包容量，装不上，只能去下个位置
                if self.w[i] > j:
                    dp[i][j] = dp[i + 1][j]
                else:
                    # 能装上货物， 装上当前货物后，再去下个位置，背包容量减去当前货物的重量
                    p1 = dp[i + 1][j - self.w[i]] + self.v[i]
                    # 能装上货物，但是不装，去下个位置
                    p2 = dp[i + 1][j]
                    dp[i][j] = max(p1, p2)

        for row in dp:
            print(row)

        return dp[0][self.m - 1]


if __name__ == '__main__':
    n = 5
    m = 10
    w = [2, 2, 6, 5, 4]
    v = [6, 3, 5, 4, 6]

    n = 7
    m = 15
    w = [3, 2, 4, 7, 3, 1, 7]
    v = [5, 6, 3, 19, 12, 4, 2]

    s = Solution()
    res = s.tbag(n, m, w, v)
    print(res)
