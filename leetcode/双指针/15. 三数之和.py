from typing import List


class Solution:
    def threeSum_brute(self, nums):
        """
        暴力枚举法求解三数之和问题：找出数组中所有和为0且不重复的三元组
        :param nums: 输入的整数数组
        :return: 包含所有符合条件的三元组的列表
        """
        n = len(nums)  # 获取数组长度，用于控制循环边界
        res = []  # 初始化结果列表，存储最终符合条件的三元组
        nums.sort()  # 对数组进行排序，目的是方便后续去重（相同元素会相邻）

        # 第一层循环：遍历三元组的第一个元素，范围到n-2（需留两个位置给j和k）
        for i in range(n - 2):
            # 去重：如果当前i不是第一个元素，且与前一个元素值相同，跳过当前i（避免重复三元组）
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 第二层循环：遍历三元组的第二个元素，起始于i+1（保证j>i），范围到n-1（需留一个位置给k）
            for j in range(i + 1, n - 1):
                # 去重：如果当前j不是i+1的第一个元素，且与前一个元素值相同，跳过当前j
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # 第三层循环：遍历三元组的第三个元素，起始于j+1（保证k>j），范围到数组末尾
                for k in range(j + 1, n):
                    # 去重：如果当前k不是j+1的第一个元素，且与前一个元素值相同，跳过当前k
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue

                    # 判断当前三元组的和是否为0，若是则加入结果列表
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.append([nums[i], nums[j], nums[k]])

        return res  # 返回最终收集的所有符合条件的三元组

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        找出数组中所有和为0且不重复的三元组

        参数:
        nums: List[int] - 输入的整数数组，可能包含重复元素

        返回:
        List[List[int]] - 所有满足条件的三元组列表，要求三元组内元素顺序无关且整体无重复
        """
        nums.sort()  # 对数组排序：1.方便后续双指针的移动逻辑；2.便于跳过重复元素去重
        result = []  # 初始化结果列表，存储最终符合条件的三元组
        n = len(nums)  # 获取数组长度，用于控制循环边界

        # 外层循环：固定三元组的第一个元素nums[i]，i的范围到n-2（需留两个位置给left和right指针）
        for i in range(n - 2):
            # 跳过重复的第一个元素：若当前i不是起始位置且与前一个元素值相同，直接跳过
            # 避免因nums[i]重复导致结果中出现重复的三元组
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 初始化双指针：left指向i的下一个元素（三元组第二个元素），right指向数组末尾（三元组第三个元素）
            left, right = i + 1, n - 1

            # 双指针遍历：在left < right的条件下寻找和为0的组合
            while left < right:
                # 计算当前三元组的和
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    # 找到和为0的三元组，加入结果列表
                    result.append([nums[i], nums[left], nums[right]])

                    # 跳过left指针的重复元素：避免因nums[left]重复导致重复三元组
                    # 需保证left < right防止越界
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # 跳过right指针的重复元素：同理避免nums[right]重复导致的重复三元组
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # 双指针同时移动：寻找下一组可能的组合（此时left和right的重复已跳过）
                    left += 1
                    right -= 1

                elif total < 0:
                    # 总和小于0，说明需要增大数值，因此左指针右移（数组已排序，右侧元素更大）
                    left += 1
                else:
                    # 总和大于0，说明需要减小数值，因此右指针左移（数组已排序，左侧元素更小）
                    right -= 1

        # 返回最终收集的所有不重复三元组
        return result


# 测试示例
if __name__ == "__main__":
    s = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print("输入:", nums)
    print("输出:", s.threeSum(nums))
    print("输出:", s.threeSum_brute(nums))
    # 输出: [[-1, -1, 2], [-1, 0, 1]]
