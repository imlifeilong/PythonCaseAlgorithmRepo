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
        return self.process(0, m)

    def process(self, index, m, ):
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

        
if __name__ == '__main__':
    n = 5
    m = 10
    w = [2, 2, 6, 5, 4]
    v = [6, 3, 5, 4, 6]
    s = Solution()
    res = s.tbag(n, m, w, v)
    print(res)
