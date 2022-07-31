class FBNX(object):
    """
    斐波那契数列
    F[n]=F[n-1]+F[n-2](n>=2,F[0]=0,F[1]=1)
    """

    def fa(self, n):
        if n == 0 or n == 1: return n
        return self.fa(n - 1) + self.fa(n - 2)

    def fb(self, n):
        """
        加缓存
        """
        cache = [0] * (n + 1)
        return self.process_b(n, cache)

    def process_b(self, n, cache):
        if n == 0 or n == 1: return n
        if cache[n] != 0: return cache[n]
        cache[n] = self.process_b(n - 1, cache) + self.process_b(n - 2, cache)
        return cache[n]

    @staticmethod
    def fc(n):
        """动态规划"""
        if n == 0: return 0
        dp = [0] * (n + 1)
        # base case
        dp[0], dp[1] = 0, 1
        # 状态转移
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    def fd(self, n):
        if n == 0: return 0
        


if __name__ == '__main__':
    fa = FBNX()
    n = 10
    print(fa.fa(n))
    print(fa.fb(n))
    print(fa.fc(n))
