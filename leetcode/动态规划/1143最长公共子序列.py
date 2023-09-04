'''

'''


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.process(text1, text2, 0, 0)

    def process(self, s1, s2, i, j):
        # 当字符串的长度越界时返回0
        if len(s1) == i or len(s2) == j:
            return 0
        # 当s1[i]和s2[j]字符相同时，长度加1，然后去各自去下一位进行比较
        if s1[i] == s2[j]:
            return 1 + self.process(s1, s2, i + 1, j + 1)

        # s1[i]不等于s2[j]时，s1的下一位和s2的当前位置与s1的当前位置和s2的下一位进行比较
        p1 = self.process(s1, s2, i + 1, j)
        p2 = self.process(s1, s2, i, j + 1)
        return max(p1, p2)

    def s(self, s1, s2):
        res = self.process_s(s1, s2, len(s1), len(s2))
        print(res)

    def process_s(self, s1, s2, m, n):
        if m == 0 or n == 0:
            return 0
        if s1[m - 1] == s2[n - 1]:
            return self.process_s(s1, s2, m - 1, n - 1) + 1
        p1 = self.process_s(s1, s2, m - 1, n)
        p2 = self.process_s(s1, s2, m, n - 1)
        return max(p1, p2)

    def longestCommonSubsequence_cache(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        cache = [[None] * (len(text2)) for _ in range(len(text1))]
        return self.process_cache(text1, text2, 0, 0, cache)

    def process_cache(self, s1, s2, i, j, cache):
        if len(s1) == i or len(s2) == j:
            return 0
        if cache[i][j] is None:
            if s1[i] == s2[j]:
                cache[i][j] = 1 + self.process_cache(s1, s2, i + 1, j + 1, cache)
            else:
                p1 = self.process_cache(s1, s2, i + 1, j, cache)
                p2 = self.process_cache(s1, s2, i, j + 1, cache)
                cache[i][j] = max(p1, p2)
        return cache[i][j]

    def longestCommonSubsequence1(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        return self.process1(text1, text2, m, n, dp)

    def process1(self, s1, s2, m, n, dp):
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        for row in dp:
            print(row)

        return dp[m][n]

    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        return self.process2(text1, text2, m, n, dp)

    def process2(self, s1, s2, m, n, dp):
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        for row in dp:
            print(row)
        return dp[0][0]


if __name__ == '__main__':
    s1 = 'ssssabcdes'
    s2 = 'sacesss'
    s1 = 'abced'
    s2 = 'acef'
    s = Solution()
    # res = s.longestCommonSubsequence(s1, s2)
    # res1 = s.longestCommonSubsequence1(s1, s2)
    # print(res1)
    # res2 = s.longestCommonSubsequence_cache(s1, s2)
    # print(res2)
    #
    # res3 = s.longestCommonSubsequence2(s1, s2)
    # print(res3)
    # s.process3(s1, s2)
    s.s(s1, s2)
