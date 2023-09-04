"""
输入: s = "A man, a plan, a canal: Panama"
输出：true
解释："amanaplanacanalpanama" 是回文串。

输入：s = "race a car"
输出：false
解释："raceacar" 不是回文串。

输入：s = " "
输出：true
解释：在移除非字母数字字符之后，s 是一个空字符串 "" 。
由于空字符串正着反着读都一样，所以是回文串。
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = [x.lower() for x in s if x.isalpha()]
        print(tmp)

        left = 0
        right = len(tmp) - 1
        while left < right:
            if tmp[left] == tmp[right]:
                left += 1
                right -= 1
            else:
                return False

        return True


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    s = "race a car"
    s = " "
    so = Solution()
    res = so.isPalindrome(s)
    print(res)
