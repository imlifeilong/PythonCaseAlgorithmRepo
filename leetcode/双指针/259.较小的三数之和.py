from typing import List


class Solution:
    def threeSumSmaller_brute(self, nums: List[int], target: int) -> int:
        count = 0
        n = len(nums)

        # 三重循环枚举所有三元组
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] < target:
                        count += 1

        return count

    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        # 对数组进行排序
        nums.sort()

        count = 0
        n = len(nums)

        # 遍历数组，固定第一个数
        for i in range(n - 2):
            left, right = i + 1, n - 1

            # 双指针寻找另外两个数
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < target:
                    # 对于固定的i和left，所有right在(left, right]区间的三元组都满足条件
                    count += right - left
                    left += 1  # 移动左指针尝试更大的和
                else:
                    right -= 1  # 和太大，移动右指针减小和

        return count


if __name__ == "__main__":
    solution = Solution()

    # 示例1
    nums1 = [-2, 0, 1, 3]
    target1 = 2
    print(f"暴力解法示例1: {solution.threeSumSmaller_brute(nums1, target1)}")  # 输出: 2
    print(f"双指针解法示例1: {solution.threeSumSmaller(nums1, target1)}")  # 输出: 2

    # 示例2
    nums2 = [1,3,0,-3,-2]
    target2 = 0
    print(f"暴力解法示例2: {solution.threeSumSmaller_brute(nums2, target2)}")  # 输出: 0
    print(f"双指针解法示例2: {solution.threeSumSmaller(nums2, target2)}")  # 输出: 0
    # 示例3
    nums3 = [0]
    target3 = 0
    print(f"暴力解法示例3: {solution.threeSumSmaller_brute(nums3, target3)}")  # 输出: 0
    print(f"双指针解法示例3: {solution.threeSumSmaller(nums3, target3)}")  # 输出: 0
