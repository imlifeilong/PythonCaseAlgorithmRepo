'''
输入：nums = [1,1,1,1,1], target = 3
输出：5
解释：一共有 5 种方法让最终目标和为 3 。
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

'''
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = self.process(0, nums, 0, target)
        print(res)

    def process(self, index, nums, cur, target):
        # 所有元素都组成表达式，并且结果等于目标值时，表示可以构成一种方法
        if index == len(nums) and cur == target:
            return 1
        # 所有元素都用完时，结果不等于目标值，不能构成
        if index == len(nums):
            return 0
        # 使用 + 时
        p1 = self.process(index + 1, nums, cur + nums[index], target)
        # 使用 - 时
        p2 = self.process(index + 1, nums, cur - nums[index], target)
        return p1 + p2


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 1, 1, 1]
    target = 3
    nums = [1]
    target = 1
    s.findTargetSumWays(nums, target)
