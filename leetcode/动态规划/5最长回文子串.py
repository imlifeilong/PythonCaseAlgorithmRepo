class Solution:
    def is_palindrome_with_collision_pointer(self, s):
        """
        双指针（对撞指针）判断字符串s是否回文
        :param s:
        :return:
        """
        left = 0
        right = len(s)

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def is_palindrome_center_expansion(self, s, left, right):
        """
        双指针（中心扩展）判断字符串s是否回文
        :param s:
        :return:
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # 退出循环时，s[left] != s[right]，所以左右指针各退一步 right-1， left+1
        # 有效长度为 (right-1) - (left+1) + 1 =  right - left - 1
        return right - left - 1

    def common_way(self, s: str):
        """
        普通暴力解法
        :param s:
        :return:
        """
        max_sub = ''
        max_lenght = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                start_index = i
                end_index = j + 1
                sub_length = end_index - start_index
                # sub = s[start_index:end_index]
                sub = s[start_index:start_index + sub_length]

                if self.is_palindrome_with_collision_pointer(sub) and sub_length > max_lenght:
                    max_sub = sub
                    max_lenght = sub_length
        print(max_sub)
        return max_sub

    def longestPalindrome(self, s: str) -> str:
        return self.process(s, 0, len(s) - 1)

    def ispalindrome(self, s):
        n = len(s)

        for i in range(n // 2 + 1):
            if s[i] != s[n - i - 1]:
                return False
        return True

    def ispalindrome1(self, s, left, right):
        '''
        判断s 在left到right上是否是回文串
        '''
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def process(self, s, i, j):
        if i > j:
            return 0
        if i == j:
            return 1
        if s[i] == s[j] and self.ispalindrome1(s, i + 1, j - 1):
            return self.process(s, i + 1, j - 1) + 2
        return max(self.process(s, i + 1, j), self.process(s, i, j - 1))

    def longestPalindrome1(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        # dp[i][j] 表示s[i:j]是否是回文串
        maxlen = 0
        for j in range(n):
            dp[j][j] = True
            for i in range(j):
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    # s[i]==s[j] 并且s[i:j]长度大于2时 依赖dp[i+1][j-1]
                    if j - i + 1 > 2:
                        dp[i][j] = dp[i + 1][j - 1]
                    else:
                        dp[i][j] = True

                    if dp[i][j] and j - i + 1 > maxlen:
                        maxlen = j - i + 1
        return maxlen


if __name__ == '__main__':
    b = 'asbdcdcdsa'
    b = 'caaccc'
    s = Solution()
    # res = s.longestPalindrome(b)
    # print(res)
    # res2 = s.longestPalindrome1(b)
    # print(res2)

    # res1 = s.ispalindrome1(b, 0, len(b) - 1)
    # print(res1)
    a = 'babad'
    s.common_way(a)
