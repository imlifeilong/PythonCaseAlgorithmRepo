class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)

        # O(N^2)
        # # 冒泡排序的思路，扫描每一个位置的值，每次只将一个0换到末尾
        # for i in range(length):
        #     # 从后向前 因为要比较 j 和 j+1所以是 从i-1开始
        #     for j in range(i - 1, -1, -1):
        #         # 如果当前值是0，就和下一位交换，如果下一位也是0 不用交换
        #         if nums[j] == 0 and nums[j + 1] != 0:
        #             nums[j], nums[j + 1] = nums[j + 1], nums[j]
        #
        # print(nums)

        # 双指针
        left = 0
        right = 0

        while right < length:
            # 右指针向右移动，如果所指的数不为0，就和left所指的值交换
            # left指向最左边第一个0的位置
            # 前几位如果不是0 left和right相等 所以这几个元素 是相当于和自己交换
            if nums[right]:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
            right += 1
        print(nums)


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    nums = [10, -1, -2, 0, 3, 0, 0, 90, 0, 1]
    s = Solution()
    s.moveZeroes(nums)
