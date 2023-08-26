from typing import List

'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0

'''


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
            遍历查找，时间复杂度O(n) 空间复杂度O(1)
        '''
        length = len(nums)
        for i in range(length):
            if target <= nums[i]:
                return i
        return length

    def searchB(self, nums: List[int], target: int) -> int:
        '''
        二分查找，时间复杂度O(logn) 空间复杂度O(1)
        '''
        left = 0
        right = len(nums) - 1
        # left <= right 表示target在[left, right]里面有效，因为right=len(num)-1
        while left <= right:
            mid = (right + left) // 2

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid

        return right + 1

    def searchB1(self, nums: List[int], target: int) -> int:
        '''二分查找'''
        left = 0
        right = len(nums)
        # 左闭右开 [left, right)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:

                left = mid + 1
            else:
                return mid

        return right


if __name__ == '__main__':
    target = 6
    data = [1, 3, 5, 6]
    s = Solution()
    index = s.searchInsert(data, target)
    print(index)
    ind = s.searchB(data, target)
    ind1 = s.searchB1(data, target)
    print(ind, ind1)
