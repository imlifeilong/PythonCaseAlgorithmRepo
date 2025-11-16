from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        找出所有和为target的不重复四元组

        参数:
        nums: List[int] - 输入数组
        target: int - 目标值

        返回:
        List[List[int]] - 所有满足条件的四元组
        """
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 3):
            # 跳过重复的第一个数
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 提前剪枝
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue

            for j in range(i + 1, n - 2):
                # 跳过重复的第二个数
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # 提前剪枝
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                    continue

                left, right = j + 1, n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        # 跳过重复元素
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1

                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return result


# 测试示例
if __name__ == "__main__":
    # 测试用例1
    nums1 = [1, 0, -1, 0, -2, 2]
    target1 = 0
    s = Solution()
    print(f"输入: nums = {nums1}, target = {target1}")
    print(f"输出: {s.fourSum(nums1, target1)}")
    # 输出: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

    # 测试用例2
    nums2 = [2, 2, 2, 2, 2]
    target2 = 8
    print(f"输入: nums = {nums2}, target = {target2}")
    print(f"输出: {s.fourSum(nums2, target2)}")
    # 输出: [[2, 2, 2, 2]]

    # 测试用例3（处理大数情况）
    nums3 = [1000000000, 1000000000, 1000000000, 1000000000]
    target3 = 0
    print(f"输入: nums = {nums3}, target = {target3}")
    print(f"输出: {s.fourSum(nums3, target3)}")
    # 输出: []
