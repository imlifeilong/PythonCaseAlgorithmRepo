"""
分析
起初一对兔子已满一个月，相当于第1个月的时候已经满1个月，根据给出的示例，如果5个月性成熟，则第6个月开始繁殖

如果3个月性成熟，得出的数列
第1个月 1
第2个月 1
第3个月 2
第4个月 3
第5个月 4
第6个月 6
第7个月 9
第8个月 13
1,1,2,3,4,6,9,13,19,28

如果f(n)表示第n个月兔子的数量，则：

可以递推为 f(n-1)+f(n-3)

如果是4个月
1,1,1,2,3,4,5,7,10,14,19,26

可以递推 f(n-1)+f(n-4)

如果是5个月
1,1,1,1,2,3,4,5,6,8,11,15,20

f(n-1)+f(n-5)

如果是6个月
1,1,1,1,1,2,3,4,5,6,7,9,12,16

f(n-1)+f(n-6)

"""


class Solution:

    def rabbits(self, month, gap):
        """
        计算gap月性成熟的兔子，第month月有几只
        :param month: 月数
        :param gap: 性成熟的月数
        :return:
        """
        cache = {}
        # return self.process(month, gap, cache)
        return self.process_dp(month, gap)

    def process(self, month, gap, cache):
        """
        递归+记忆搜索 容易递归溢出
        """
        if month not in cache:
            if month == 0:
                cache[month] = 1
            elif month < gap:
                cache[month] = 1
            else:
                cache[month] = self.process(month - 1, gap, cache) + self.process(month - gap, gap, cache)

        return cache[month]

    def process_dp(self, month, gap):
        # 动态规划
        dp = [0 if i >= gap else 1 for i in range(month + 1)]
        # print(dp)
        # dp[n] 表示第n月时兔子的数量
        for n in range(gap, month + 1):
            dp[n] = dp[n - 1] + dp[n - gap]

        return dp[month]


if __name__ == '__main__':
    month = 24
    gap = 4
    s = Solution()
    # s.rabbits(month, gap)

    for i in range(1, month + 1):
        res = s.rabbits(i, gap)
        print(f"第{i}个月 兔子数量 {res}")
