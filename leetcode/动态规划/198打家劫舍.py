"""
输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。

"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        res = self.process(0, nums)
        print(res)
        index = len(nums)
        res1 = self.process1(index - 1, nums)
        print(res1)
        cache = [None] * index
        res2 = self.process_cache(index - 1, nums, cache)
        print(res2)
        res3 = self.process_dp(nums)

    def process(self, index, nums):
        if index == len(nums):
            return 0
        if index == len(nums) - 1:
            return nums[index]
        return max(self.process(index + 1, nums), self.process(index + 2, nums) + nums[index])

    def process1(self, index, nums):
        if index < 0:
            return 0
        if index == 0:
            return nums[index]
        return max(self.process1(index - 1, nums), self.process1(index - 2, nums) + nums[index])

    def process_cache(self, index, nums, cache):
        if cache[index]:
            return cache[index]
        if index < 0:
            cache[index] = 0
        elif index == 0:
            cache[index] = nums[index]
        else:
            cache[index] = max(self.process_cache(index - 1, nums, cache),
                               self.process_cache(index - 2, nums, cache) + nums[index])
        return cache[index]

    def process_dp(self, nums):
        index = len(nums)
        dp = [None] * index

        for i in range(-1, index):
            if i < 0:
                dp[i] = 0
            elif i == 0:
                dp[i] = nums[i]
            else:
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        print(dp[index - 1])


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 1]
    # nums = [2, 7, 9, 3, 1]
    s.rob(nums)
