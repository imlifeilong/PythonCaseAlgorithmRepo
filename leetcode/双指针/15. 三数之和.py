from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        找出所有和为0的不重复三元组

        参数:
        nums: List[int] - 输入数组

        返回:
        List[List[int]] - 所有满足条件的三元组
        """
        nums.sort()  # 先排序
        result = []
        n = len(nums)

        for i in range(n - 2):
            # 跳过重复元素
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 双指针
            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # 跳过重复元素
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result


# 测试示例
if __name__ == "__main__":
    s = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print("输入:", nums)
    print("输出:", s.threeSum(nums))
    # 输出: [[-1, -1, 2], [-1, 0, 1]]
