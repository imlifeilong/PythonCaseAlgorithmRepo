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

    def process(self, index, nums):
        if index == len(nums):
            return 0
        if index == len(nums) - 1:
            return nums[index]
        return max(self.process(index + 1, nums), self.process(index + 2, nums) + nums[index])


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 1]
    nums = [2, 7, 9, 3, 1]
    s.rob(nums)
