"""
K数之和
-1 0 1 2 -1 -4
3
0


此题问方案数量，所以想到动态规划：使用三个for循环，时间复杂度为O(n * k * target)
1、状态的定义：我们定义矩阵元素 dp[h][i][j] 代表了从前 h 个元素中选取 i 个，
使其和为 j 有几种方法。dp是一个三维矩阵。注意初始化时候分配的空间是(n + 1) * (k + 1) * (target + 1)，
这里 n 代表数组 a 的长度

2、初始化：不管给我们几个数，我们总有一种办法选取 0 个数（也就是啥都不选）使其的和为0，所以 dp[h][0][0] 我们初始化为 1

3、状态转移方程：如何把 dp[h][i][j] 和更小的问题联系起来呢？其实和经典的01背包问题很相似
现在我们要在前 h 个数中选 i 个数使它们的和为 j。
如果第 h 个元素也就是 a[h - 1] 它小于等于我们的目标 j，
我们可以选它也可以不选它。如果我们选它：那我们要在前 h - 1 个数中选出 i - 1个数，
使它们的和为 j - a[h - 1]。如果我们不选它：那我们得在前 h - 1 个数中就选出 i 个数和为 j。
这两种情况都会为dp[h][i][j] 的总方案数做贡献，所以 dp[h][i][j] = dp[h - 1][i - 1][j - a[h - 1]] + dp[h - 1][i][j]
如果第 h 个元素a[h - 1] 它大于我们的目标 j，我们肯定不能选它，不然和就超出 j 了。所以我们只能在前 h - 1 个数中就选出 i 个数和为 j。此时 dp[h][i][j] = dp[h - 1][i][j]

4、返回dp[n][k][target]，意味着在前 n 个元素中选取 k 个，使其和为 target 有几种方法，也就是我们想要的答案

"""


class KSum:
    def main(self, data, k, target):
        tmp = []
        self.reault_set = set()
        self.data = data
        self.target = target
        self.process(0, 0, k, tmp)
        print(self.reault_set)
        # dp = [[0] for i in range(k)]
        # self.process_b(0, 0, k, tmp)

    def process(self, index, total, k, tmp):
        """
        第index个数的和时total
        :param index:
        :param total:
        :param data:
        :param k:
        :param target:
        :return:
        """
        # # 当k个数的和为target时，方案数+1
        if k == 0 and total == self.target:
            tmp.sort()
            self.reault_set.add(tuple(tmp))
            print(tmp)
            return 1

        if index >= len(self.data) or (k <= 0 and total != self.target):
            return 0

        cur = self.data[index]
        print(f'当前值 {cur} 还剩{k - 1}')

        # 选择当前值
        tmp.append(cur)
        p1 = self.process(index + 1, total + cur, k - 1, tmp)
        # 不选当前值，回溯
        tmp.pop()

        # 不选当前值
        p2 = self.process(index + 1, total, k, tmp)

        return p1 + p2

    def process_b(self, index, total, k, tmp):
        """
        第index个数的和时total
        :param index:
        :param total:
        :param data:
        :param k:
        :param target:
        :return:
        """
        # # 当k个数的和为target时，方案数+1
        if k == 0 and total == self.target:
            tmp.sort()
            self.reault_set.add(tuple(tmp))
            print(tmp)
            return 1

        if index >= len(self.data) or (k <= 0 and total != self.target):
            return 0

        cur = self.data[index]
        print(f'当前值 {cur} 还剩{k - 1}')

        # 选择当前值
        tmp.append(cur)
        p1 = self.process_b(index + 1, total + cur, k - 1, tmp)
        # 不选当前值，回溯
        tmp.pop()

        # 不选当前值
        p2 = self.process_b(index + 1, total, k, tmp)
        return p1 + p2


data = [int(i) for i in '-1 0 1 2 -1 -4'.split()]
k = 3
target = 0

# data = [int(i) for i in '2 7 11 15'.split()]
# k = 2
# target = 9

ks = KSum()
ks.main(data, k, target)
