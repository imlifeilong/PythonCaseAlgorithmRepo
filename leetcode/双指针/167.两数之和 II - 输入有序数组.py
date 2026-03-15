# 从typing模块导入List类型，用于进行数组类型注解
from typing import List


# 定义解题类，包含两种解决有序数组两数之和问题的方法
class Solution:
    """
    有序数组两数之和问题的解题类
    提供暴力枚举和双指针两种解法
    """

    def twoSum_brute(self, numbers: List[int], target: int) -> List[int]:
        """
        暴力枚举法求解有序数组两数之和
        :param numbers: 非递减排序的整数数组（输入保证有序）
        :param target: 目标和值，题目保证存在唯一解
        :return: 满足条件的两个数的下标（下标从1开始计数，而非0）
        """
        # 获取数组长度，用于控制循环边界
        n = len(numbers)

        # 外层循环：遍历第一个数的索引，范围是0到n-2（预留j的位置，避免越界）
        for i in range(n - 1):
            # 内层循环：遍历第二个数的索引，从i+1开始（避免重复计算同一对元素）
            for j in range(i + 1, n):
                # 判断当前两数之和是否等于目标值
                if numbers[i] + numbers[j] == target:
                    # 题目要求下标从1开始，因此返回时索引各加1
                    return [i + 1, j + 1]

        # 题目明确保证存在唯一解，此返回语句实际不会被执行，仅用于语法完整性
        return []

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        双指针法求解有序数组两数之和（最优解法，时间复杂度O(n)）
        利用数组非递减有序的特性，通过指针移动高效查找目标组合
        :param numbers: 非递减排序的整数数组（输入保证有序）
        :param target: 目标和值，题目保证存在唯一解
        :return: 满足条件的两个数的下标（下标从1开始计数，而非0）
        """
        # 初始化双指针：左指针指向数组起始位置（最小元素），右指针指向数组末尾（最大元素）
        left, right = 0, len(numbers) - 1

        # 循环条件：左指针必须在右指针左侧（保证两个指针不重合，不选取同一元素）
        while left < right:
            # 计算当前双指针指向元素的和
            current_sum = numbers[left] + numbers[right]

            # 情况1：当前和等于目标值，找到唯一解
            if current_sum == target:
                # 转换为题目要求的1开始下标，返回结果
                return [left + 1, right + 1]
            # 情况2：当前和小于目标值
            elif current_sum < target:
                # 数组非递减有序，左指针右移可增大两数之和，继续查找
                left += 1
            # 情况3：当前和大于目标值
            else:
                # 数组非递减有序，右指针左移可减小两数之和，继续查找
                right -= 1

        # 题目明确保证存在唯一解，此返回语句实际不会被执行，仅用于语法完整性
        return []


# 主程序入口：当脚本直接运行时，执行以下测试代码
if __name__ == "__main__":
    # 创建解题类实例
    solution = Solution()

    # 测试示例1：基础有序数组
    numbers1 = [2, 7, 11, 15]  # 有序数组
    target1 = 9  # 目标和
    result1 = solution.twoSum_brute(numbers1, target1)  # 暴力解法求解
    result1 = solution.twoSum(numbers1, target1)  # 双指针解法求解（覆盖上方暴力解法结果）
    print(f"Test 1: {result1}")  # 输出测试结果，预期为[1,2]

    # 测试示例2：三个元素的有序数组
    numbers2 = [2, 3, 4]  # 有序数组
    target2 = 6  # 目标和
    result2 = solution.twoSum_brute(numbers2, target2)  # 暴力解法求解
    result2 = solution.twoSum(numbers2, target2)  # 双指针解法求解（覆盖上方暴力解法结果）
    print(f"Test 2: {result2}")  # 输出测试结果，预期为[1,3]

    # 测试示例3：包含负数的有序数组
    numbers3 = [-1, 0]  # 有序数组
    target3 = -1  # 目标和
    result3 = solution.twoSum_brute(numbers3, target3)  # 暴力解法求解
    result3 = solution.twoSum(numbers3, target3)  # 双指针解法求解（覆盖上方暴力解法结果）
    print(f"Test 3: {result3}")  # 输出测试结果，预期为[1,2]
