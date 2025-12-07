from typing import List


class Solution:
    def removeElement_brute(self, nums: List[int], val: int) -> int:
        size = len(nums)
        i = 0
        while i < size:
            if nums[i] == val:  # 发现需要移除的元素
                for j in range(i + 1, size):  # 将后续元素前移
                    nums[j - 1] = nums[j]
                i -= 1  # 因为下标i以后的数值都向前移动了一位，所以i也向前移动一位
                size -= 1  # 此时数组的大小减1
            i += 1
        return size

    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0  # 慢指针：新数组的末尾
        for fast in range(len(nums)):  # 快指针遍历数组
            if nums[fast] != val:  # 找到有效元素
                nums[slow] = nums[fast]  # 赋值给慢指针位置
                slow += 1  # 慢指针前进
        return slow  # 慢指针的位置即为新长度


if __name__ == "__main__":
    solution = Solution()

    # 示例1
    nums1 = [3, 2, 2, 3]
    val1 = 3
    len1 = solution.removeElement_brute(nums1, val1)
    len1 = solution.removeElement(nums1, val1)
    print(f"示例1: nums = [3,2,2,3], val = 3")
    print(f"返回长度: {len1}")
    print(f"修改后的数组: {nums1[:len1]}")
    print()

    # 示例2
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    len2 = solution.removeElement_brute(nums2, val2)
    len2 = solution.removeElement(nums2, val2)
    print(f"示例2: nums = [0,1,2,2,3,0,4,2], val = 2")
    print(f"返回长度: {len2}")
    print(f"修改后的数组: {nums2[:len2]}")
