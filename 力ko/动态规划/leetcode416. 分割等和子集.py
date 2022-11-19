'''
输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。
'''
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 总和不能均分，一定不能分割成两部分
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) / 2
        print(target)
        res = self.process(0, nums, target)
        print(res)

    def process(self, index, nums, target):
        # 目标值为0时
        if target == 0:
            return True
        # 当过了最后的位置时，目标值还不为0
        if index == len(nums):
            return False

        # 当前值已经大于目标值，只能去下一位置
        if target - nums[index] < 0:
            return self.process(index + 1, nums, target)

        # 选择当前值， 选择后去下一位置，目标值减去当前值
        p1 = self.process(index + 1, nums, target - nums[index])
        # 不选当前值，去下一位置
        p2 = self.process(index + 1, nums, target)
        return p1 or p2


if __name__ == '__main__':
    s = Solution()
    nums = [1, 5, 11, 5]
    nums = [1, 2, 3, 5, 1, 2]
    s.canPartition(nums)
