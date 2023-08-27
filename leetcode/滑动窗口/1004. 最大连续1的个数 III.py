"""
给定一个二进制数组 nums 和一个整数 k，如果可以翻转最多 k 个 0 ，则返回 数组中连续 1 的最大个数
题意理解
求最长的子串，要求该子串种最多包含k个0
"""


class Solution:
    def longestOnes(self, nums, k):
        # 求data中找出一个最长的子串，该子串中最多包含k个0
        n = len(nums)
        result = 0  # 结果
        left = 0
        right = 0
        count = 0  # 记录子串中0的个数
        while right < n:
            # 移动右指针，统计窗口内0的个数
            if nums[right] == 0:
                count += 1
            # print(data[left:right + 1])
            # 每移动一次right，统计一次，就需要判断窗口内0的个数
            # 如果 0的个数已经超过k，必须移动left，来控制0的个数小于等于k
            while count > k:
                # left移动的过程中遇见0，则0的个数-1，继续移动left，直到0的个数小于等于K时停止
                # print(data[left:right + 1])
                if nums[left] == 0:
                    count -= 1
                left += 1
            # 记录满足条件的子串的长度，并且和之前的满足条件的子串进行对比，取较长的长度
            result = max(result, right - left + 1)

            right += 1
        print(result)
        return result


if __name__ == '__main__':
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2

    # nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    # k = 3
    s = Solution()
    s.longestOnes(nums, k)
