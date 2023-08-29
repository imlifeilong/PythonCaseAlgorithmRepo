class Solution:
    def longestPalindrome(self, s):
        if len(s) == 1:
            return s

        maxlen = 0
        res = ''
        for i in range(len(s) + 1):
            for j in range(i):
                tmp = s[j:i]
                if self.isPalindrome(tmp):
                    if len(tmp) > maxlen:
                        res = tmp
                        maxlen = len(tmp)

        return res

    def isPalindrome(self, s):
        """判断s是不是回文串，连续的"""
        left = 0
        right = len(s)
        while left < right:
            if s[left] != s[right - 1]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == '__main__':
    s = 'babad'
    # s = "cbbd"
    # s = 'a'
    # s = 'aa'
    s = ''
    obj = Solution()
    res = obj.longestPalindrome(s)
    print('==========', res)
