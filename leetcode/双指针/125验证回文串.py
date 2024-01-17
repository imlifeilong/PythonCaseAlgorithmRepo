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
        # 去掉非字母数字字符
        tmp = [x.lower() for x in s if x.isalnum()]

        left = 0
        right = len(tmp) - 1
        # 如果字符长度时奇数，不需要比较中间位置
        # 如果字符长度时偶数，没有中间位置
        # 所以使用<进行比较
        while left < right:
            if tmp[left] == tmp[right]:
                left += 1
                right -= 1
            else:
                return False

        return True


if __name__ == '__main__':
    s = "1A man, a plan, a canal: Panama1"
    s = "raca a car"
    # s = " "
    so = Solution()
    res = so.isPalindrome(s)
    print(res)
