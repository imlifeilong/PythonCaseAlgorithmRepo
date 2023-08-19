"""
题目：给定一个二进制数组，你可以最多将 1 个 0 翻转为 1，找出其中最大连续 1 的个数。

题意可以转换成 求最长的子串，要求该子串最多包含1个0
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        n = len(nums)
        left = 0
        rigth = 0
        count = 0
        result = 0
        while rigth < n:
            # 统计left和right种的0的个数
            if nums[rigth] == 0:
                count += 1

            # 如果0的个数大于1，则需要移动left，控制0的个数保持在1个
            while count > 1:
                # 如果left指向的值为0，则记录0的个数-1
                if nums[left] == 0:
                    count -= 1
                left += 1
            # 记录left和right的长度，并且与之前的比较，取长度较长的
            result = max(result, rigth - left + 1)

            rigth += 1
        print(result)
        return result


if __name__ == '__main__':
    nums = [1, 0, 1, 1, 0]
    s = Solution()
    s.findMaxConsecutiveOnes(nums)
