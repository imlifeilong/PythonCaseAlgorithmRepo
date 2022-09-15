class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.process(s, 0, len(s) - 1)

    def process(self, s, m, n):
        if m < 0 or n > len(s) or m > n:
            return 0
        if s[m] == s[n]:
            return self.process(s, m + 1, n - 1) + 2
        return max(self.process(s, m + 1, n), self.process(s, m, n - 1))

    def longestPalindromeSubseq1(self, s: str) -> int:
        n = len(s)
        cache = [[0] * (n + 1) for _ in range(n + 1)]
        return self.process(s, 0, len(s) - 1, cache)

    def process1(self, s, m, n, cache):
        if m < 0 or n > len(s) or m > n:
            return 0

        if cache[m][n] !=0:
            pass

        if s[m] == s[n]:
            return self.process1(s, m + 1, n - 1) + 2
        return max(self.process1(s, m + 1, n), self.process1(s, m, n - 1))


if __name__ == '__main__':
    s = Solution()

    data = '123321123132123'
    res = s.longestPalindromeSubseq(data)
    print(res)
