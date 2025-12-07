# 从typing模块导入List类型，用于类型注解
from typing import List


class Solution:
    def threeSumClosest_brute(self, nums, target):
        """
        暴力枚举法求最接近目标值的三数之和
        思路：枚举所有可能的三元组组合，计算其和与目标值的差值，记录最小差值对应的和

        参数:
        nums: List[int] - 输入的整数数组
        target: int - 目标值

        返回:
        int - 最接近目标值的三数之和
        """
        n = len(nums)  # 获取数组长度
        # 初始化最接近的和为前三个元素的和（初始候选值）
        closest_sum = nums[0] + nums[1] + nums[2]
        # 初始化最小差值为初始和与目标值的绝对差
        min_diff = abs(closest_sum - target)

        # 三层循环枚举所有i<j<k的三元组（暴力遍历所有组合）
        for i in range(n - 2):          # 第一个数的索引i（范围到n-3，留两个位置给j和k）
            for j in range(i + 1, n - 1):  # 第二个数的索引j（必须大于i，范围到n-2）
                for k in range(j + 1, n):  # 第三个数的索引k（必须大于j）
                    current_sum = nums[i] + nums[j] + nums[k]  # 当前三元组的和
                    current_diff = abs(current_sum - target)   # 当前和与目标值的绝对差

                    # 如果当前差值更小，更新最小差值和最接近的和
                    if current_diff < min_diff:
                        min_diff = current_diff
                        closest_sum = current_sum

                    # 如果差值为0（完全匹配目标值），直接返回（无法更接近）
                    if current_diff == 0:
                        return current_sum

        return closest_sum  # 返回最终找到的最接近和

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        排序+双指针法求最接近目标值的三数之和（优化解法）
        思路：先排序数组，固定第一个数，用双指针遍历剩余元素，根据和的大小调整指针位置，降低时间复杂度

        参数:
        nums: List[int] - 输入的整数数组
        target: int - 目标值

        返回:
        int - 最接近目标值的三数之和
        """
        nums.sort()  # 对数组排序，为双指针操作铺垫
        n = len(nums)  # 获取数组长度
        closest_sum = nums[0] + nums[1] + nums[2]  # 初始化最接近的和

        # 遍历第一个数的索引i（固定第一个数）
        for i in range(n - 2):
            # 跳过重复的i（优化：避免重复计算相同的三元组组合）
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1  # 左指针（i的下一个元素）、右指针（数组末尾）

            # 双指针遍历剩余元素，寻找最优的后两个数
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]  # 当前三元组的和

                # 如果当前和等于目标值，直接返回（完全匹配）
                if current_sum == target:
                    return current_sum

                # 如果当前和更接近目标值，更新最接近的和
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                # 根据当前和与目标值的大小关系调整指针：
                # 和偏小则左指针右移（增大和），和偏大则右指针左移（减小和）
                if current_sum < target:
                    left += 1
                else:
                    right -= 1

        return closest_sum  # 返回最终找到的最接近和


# 测试示例（当模块作为主程序运行时执行）
if __name__ == "__main__":
    # 测试用例1：常规情况（存在接近目标值的组合）
    nums1 = [-1, 2, 1, -4]
    target1 = 1
    s = Solution()  # 创建Solution类实例
    print(f"输入: nums = {nums1}, target = {target1}")
    print(f"双指针解法输出: {s.threeSumClosest(nums1, target1)}")  # 预期输出2（-1+2+1=2，最接近1）
    print(f"暴力解法输出: {s.threeSumClosest_brute(nums1, target1)}")  # 预期输出2

    # 测试用例2：所有元素相同的情况
    nums2 = [0, 0, 0]
    target2 = 1
    print(f"\n输入: nums = {nums2}, target = {target2}")
    print(f"双指针解法输出: {s.threeSumClosest(nums2, target2)}")  # 预期输出0（唯一可能的和）
    print(f"暴力解法输出: {s.threeSumClosest_brute(nums2, target2)}")  # 预期输出0

    # 测试用例3：目标值远小于数组元素和的情况
    nums3 = [1, 1, 1, 0]
    target3 = -100
    print(f"\n输入: nums = {nums3}, target = {target3}")
    print(f"双指针解法输出: {s.threeSumClosest(nums3, target3)}")  # 预期输出2（0+1+1=2，最接近-100）
    print(f"暴力解法输出: {s.threeSumClosest_brute(nums3, target3)}")  # 预期输出2