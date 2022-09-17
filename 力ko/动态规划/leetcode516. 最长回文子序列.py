class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.process(s, 0, len(s) - 1)

    def process(self, s, m, n):
        if m < 0 or n > len(s) or m > n:
            return 0
        if m == n:
            return 1
        if s[m] == s[n]:
            return self.process(s, m + 1, n - 1) + 2
        return max(self.process(s, m + 1, n), self.process(s, m, n - 1))

    def longestPalindromeSubseq1(self, s: str) -> int:
        n = len(s)
        cache = [[0] * (n + 1) for _ in range(n + 1)]
        return self.process1(s, 0, len(s) - 1, cache)

    def process1(self, s, m, n, cache):
        """
        带缓存的，符串在m~n上的最长回文子序列
        """
        if m < 0 or n > len(s) or m > n:
            return 0
        if m == n:
            return 1

        if cache[m][n] != 0:
            return cache[m][n]
        if s[m] == s[n]:
            result = self.process1(s, m + 1, n - 1, cache) + 2
        else:
            result = max(self.process1(s, m + 1, n, cache), self.process1(s, m, n - 1, cache))
        return result

    def longestPalindromeSubseq2(self, s: str) -> int:
        """
        动态规划
        :param s:
        :return:
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        # 因为每格都依赖下一行的值和上一列的值，所以从下往上，从左往右填值
        for i in range(n - 1, -1, -1):
            # 每个字符串自己就是长度为1的回文序列
            dp[i][i] = 1
            # 只需要对角线右边的值，所以从i+1开始
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]


if __name__ == '__main__':
    s = Solution()

    data = "euazbipzncptldueeuechubrcourfpftcebikrxhybkymimgvldiwqvkszfycvqyvtiwfckexmowcxztkfyzqovbtmzpxojfofbvwnncajvrvdbvjhcrameamcfmcoxryjukhpljwszknhiypvyskmsujkuggpztltpgoczafmfelahqwjbhxtjmebnymdyxoeodqmvkxittxjnlltmoobsgzdfhismogqfpfhvqnxeuosjqqalvwhsidgiavcatjjgeztrjuoixxxoznklcxolgpuktirmduxdywwlbikaqkqajzbsjvdgjcnbtfksqhquiwnwflkldgdrqrnwmshdpykicozfowmumzeuznolmgjlltypyufpzjpuvucmesnnrwppheizkapovoloneaxpfinaontwtdqsdvzmqlgkdxlbeguackbdkftzbnynmcejtwudocemcfnuzbttcoew"
    # data = 'abbcd'
    # res = s.longestPalindromeSubseq(data)
    # print(res)
    # res1 = s.longestPalindromeSubseq1(data)
    # print(res1)
    res2 = s.longestPalindromeSubseq2(data)
    print(res2)
