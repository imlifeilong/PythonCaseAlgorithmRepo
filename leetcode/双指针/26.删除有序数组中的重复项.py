from typing import List


class Solution:
    def removeDuplicates_brute(self, nums: List[int]) -> int:
        if not nums:
            return 0

        i = 0
        # 使用while循环，因为数组长度在动态变化[citation:4]
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                # 发现重复，使用pop(i)移除重复元素
                nums.pop(i + 1)
                # 注意：i不递增，继续检查当前位置
            else:
                i += 1  # 没有重复，检查下一个
        return len(nums)

    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        slow = 0  # 慢指针
        # 快指针从1开始遍历[citation:7]
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:  # 发现不重复元素
                slow += 1
                nums[slow] = nums[fast]  # 赋值[citation:1]
        return slow + 1  # 返回新长度[citation:8]


if __name__ == "__main__":
    solution = Solution()

    # 示例 1
    nums1 = [1, 1, 2]
    len1 = solution.removeDuplicates_brute(nums1)
    len1 = solution.removeDuplicates(nums1)
    print(f"新长度: {len1}")
    print(f"修改后数组: {nums1[:len1]}")

    # 示例 2
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    len2 = solution.removeDuplicates_brute(nums2)
    len2 = solution.removeDuplicates(nums2)
    print(f"新长度: {len2}")
    print(f"修改后数组: {nums2[:len2]}")
