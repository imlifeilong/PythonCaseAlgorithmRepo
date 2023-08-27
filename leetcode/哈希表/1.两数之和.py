from typing import List

'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

 

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]

'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        mapping = {}
        for i in range(len(nums)):
            sub = target - nums[i]
            # 如果当前数
            if nums[i] in mapping:
                return [mapping[nums[i]], i]
            # 记录当前数和目标差 与 当前坐标映射
            if sub not in mapping:
                mapping[sub] = i


if __name__ == '__main__':
    s = Solution()
    nums = [3, 2, 4, 2, 7, 11, 15]
    target = 9
    res = s.twoSum(nums, target)
    print(res)
