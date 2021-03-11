from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''双指针，快慢指针，时间复杂度O(n) 空间复杂度O(1)'''
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        print(index, nums)
        return index


if __name__ == '__main__':
    nums = [3, 2, 2, 3]
    val = 2
    s = Solution()
    s.removeElement(nums, val)
