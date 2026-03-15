from typing import List


class Solution:

    # 方法一：暴力解法
    def sortedSquares_brute(self, nums: List[int]) -> List[int]:
        """
        暴力解法：先计算每个元素的平方，然后对结果进行排序。

        时间复杂度: O(N log N)，其中 N 是数组 nums 的长度。
        - 计算平方需要 O(N) 的时间。
        - 排序需要 O(N log N) 的时间。
        总体复杂度由排序决定。

        空间复杂度: O(log N) 或 O(N)，取决于排序算法的实现。
        """
        # 1. 遍历数组，计算每个元素的平方并原地替换
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]

        # 2. 对平方后的数组进行排序
        nums.sort()

        # 3. 返回排序后的结果
        return nums

    # 方法二：双指针解法 (更优解)
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        双指针解法：利用原数组的有序性，从两端向中间比较，构建结果数组。

        核心思想：
        一个非递减数组的平方，其最大值一定出现在原数组的两端（最左或最右）。
        因此，我们可以用两个指针分别指向数组的开头和结尾，比较它们的平方值，
        将较大的平方值从结果数组的末尾开始向前填充。

        时间复杂度: O(N)，其中 N 是数组 nums 的长度。
        - 只需要遍历数组一次。

        空间复杂度: O(N)，用于存储结果数组。
        """
        n = len(nums)
        result = [0] * n  # 创建一个与输入数组等长的结果数组，用于存储平方值

        left, right = 0, n - 1  # 初始化左右指针，分别指向数组的首尾
        pos = n - 1  # 初始化结果数组的填充位置指针，从末尾开始

        # 当左指针在右指针左侧或重合时，继续循环
        while left <= right:
            # 计算左右指针所指元素的平方
            left_square = nums[left] * nums[left]
            right_square = nums[right] * nums[right]

            # 比较两个平方值的大小
            if left_square > right_square:
                # 如果左指针的平方更大，则将其放入结果数组的当前位置
                result[pos] = left_square
                left += 1  # 左指针向右移动，寻找下一个可能的最大值
            else:
                # 如果右指针的平方更大或相等，则将其放入结果数组的当前位置
                result[pos] = right_square
                right -= 1  # 右指针向左移动，寻找下一个可能的最大值

            pos -= 1  # 结果数组的填充位置向前移动一位

        # 返回构建好的结果数组
        return result


def main():
    # 准备两个测试用例
    nums1 = [-4, -1, 0, 3, 10]
    nums2 = [-7, -3, 2, 3, 11]

    # 创建Solution类的实例
    solution = Solution()

    # --- 测试暴力解法 ---
    print("--- 测试暴力解法 ---")
    # 注意：暴力解法会修改原始数组，因此每次调用时最好使用一个副本
    result1 = solution.sortedSquares_brute(nums1.copy())
    print(f"输入 {nums1} 的结果:", result1)

    result2 = solution.sortedSquares_brute(nums2.copy())
    print(f"输入 {nums2} 的结果:", result2)
    print("-" * 20)

    # --- 测试双指针解法 ---
    print("\n--- 测试双指针解法 ---")
    result1 = solution.sortedSquares(nums1)
    print(f"输入 {nums1} 的结果:", result1)

    result2 = solution.sortedSquares(nums2)
    print(f"输入 {nums2} 的结果:", result2)
    print("-" * 20)


# 当该脚本作为主程序运行时，执行main函数
if __name__ == "__main__":
    main()
