# 导入类型注解模块，用于标注函数参数和返回值的类型（提升代码可读性）
from typing import List


class Solution:
    """
    接雨水问题的三种解法封装类：
    1. trap_brute: 暴力解法（直观但低效）
    2. trap_dp: 动态规划解法（空间换时间）
    3. trap: 双指针解法（最优解，时间+空间效率最高）
    """

    def trap_brute(self, height: List[int]) -> int:
        """
        暴力解法：逐个位置计算能接的雨水量
        核心思路：
            对每个位置i，能接水量 = min(左侧最大高度, 右侧最大高度) - 当前高度
            遍历每个位置，分别向左/右找最大高度，累加总水量
        时间复杂度：O(n²) （每个位置需遍历左右，共n个位置）
        空间复杂度：O(1) （仅用常量级变量）
        :param height: 存储柱子高度的列表
        :return: 总共能接的雨水量
        """
        n = len(height)
        # 边界条件：无柱子时接水量为0
        if n == 0:
            return 0

        ans = 0  # 存储总接水量

        # 遍历每个柱子位置，计算该位置的接水量
        for i in range(n):
            left_max = 0  # 位置i左侧（含i）的最大高度
            right_max = 0  # 位置i右侧（含i）的最大高度

            # 向左遍历（从i到0），找到左侧最大高度
            for j in range(i, -1, -1):
                left_max = max(left_max, height[j])

            # 向右遍历（从i到n-1），找到右侧最大高度
            for j in range(i, n):
                right_max = max(right_max, height[j])

            # 累加当前位置的接水量（若结果为负，说明接不到水，min差值自然为0）
            ans += min(left_max, right_max) - height[i]

        return ans

    def trap_dp(self, height: List[int]) -> int:
        """
        动态规划解法：预处理左右最大高度数组，避免暴力法的重复计算
        核心思路：
            1. 预先用left_max数组存储每个位置左侧的最大高度
            2. 预先用right_max数组存储每个位置右侧的最大高度
            3. 遍历每个位置，用预处理数组计算接水量
        时间复杂度：O(n) （三次线性遍历）
        空间复杂度：O(n) （存储两个预处理数组）
        :param height: 存储柱子高度的列表
        :return: 总共能接的雨水量
        """
        n = len(height)
        if n == 0:
            return 0

        # 初始化预处理数组：left_max[i]表示i位置及左侧的最大高度
        left_max = [0] * n
        # right_max[i]表示i位置及右侧的最大高度
        right_max = [0] * n

        # 第一步：从左到右构建left_max数组
        left_max[0] = height[0]  # 第一个位置的左侧最大高度是自身
        for i in range(1, n):
            # 当前位置的left_max = 前一个位置的left_max 和 当前高度的较大值
            left_max[i] = max(left_max[i - 1], height[i])

        # 第二步：从右到左构建right_max数组
        right_max[n - 1] = height[n - 1]  # 最后一个位置的右侧最大高度是自身
        for i in range(n - 2, -1, -1):
            # 当前位置的right_max = 后一个位置的right_max 和 当前高度的较大值
            right_max[i] = max(right_max[i + 1], height[i])

        # 第三步：遍历计算总接水量
        ans = 0
        for i in range(n):
            ans += min(left_max[i], right_max[i]) - height[i]

        return ans

    def trap(self, height: List[int]) -> int:
        """
        双指针最优解法：空间复杂度优化至O(1)
        核心思路：
            1. 左右指针分别指向数组两端，向中间移动
            2. 维护left_max（左指针左侧最大高度）、right_max（右指针右侧最大高度）
            3. 若height[left] < height[right]：左侧高度更小，接水量由left_max决定
               - 若当前height[left] >= left_max，更新left_max（无法接水）
               - 否则，累加接水量（left_max - height[left]）
               - 左指针右移
            4. 反之：右侧高度更小，接水量由right_max决定，逻辑同上
        时间复杂度：O(n) （一次线性遍历）
        空间复杂度：O(1) （仅用常量级变量）
        :param height: 存储柱子高度的列表
        :return: 总共能接的雨水量
        """
        n = len(height)
        if n == 0:
            return 0

        left = 0  # 左指针：初始指向数组最左端
        right = n - 1  # 右指针：初始指向数组最右端
        left_max = 0  # 左指针左侧的最大高度（实时维护）
        right_max = 0  # 右指针右侧的最大高度（实时维护）
        ans = 0  # 总接水量

        # 左右指针未相遇时循环
        while left < right:
            # 左侧柱子高度 < 右侧柱子高度：处理左指针
            if height[left] < height[right]:
                # 当前左指针高度 >= 左侧最大高度：更新最大高度（无法接水）
                if height[left] >= left_max:
                    left_max = height[left]
                # 当前高度 < 左侧最大高度：可以接水，累加接水量
                else:
                    ans += left_max - height[left]
                left += 1  # 左指针右移
            # 右侧柱子高度 <= 左侧柱子高度：处理右指针
            else:
                # 当前右指针高度 >= 右侧最大高度：更新最大高度（无法接水）
                if height[right] >= right_max:
                    right_max = height[right]
                # 当前高度 < 右侧最大高度：可以接水，累加接水量
                else:
                    ans += right_max - height[right]
                right -= 1  # 右指针左移

        return ans


def main():
    """主函数：测试接雨水的三种解法（当前测试暴力+DP解法，可注释切换）"""
    solution = Solution()  # 创建解法类实例

    # 示例 1：经典测试用例（预期输出：6）
    height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    result1 = solution.trap_brute(height1)  # 暴力解法计算
    result1 = solution.trap_dp(height1)  # 动态规划解法覆盖结果
    # result1 = solution.trap(height1)      # 双指针解法（可取消注释测试）
    print(f"示例 1 结果: {result1}")

    # 示例 2：右侧有更高柱子的测试用例（预期输出：9）
    height2 = [4, 2, 0, 3, 2, 5]
    result2 = solution.trap_brute(height2)
    result2 = solution.trap_dp(height2)
    # result2 = solution.trap(height2)
    print(f"示例 2 结果: {result2}")

    # 示例 3：调整初始柱子高度的测试用例（预期输出：10）
    height3 = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1, 2, 1]
    result3 = solution.trap_brute(height3)
    result3 = solution.trap_dp(height3)
    # result3 = solution.trap(height3)
    print(f"示例 3 结果: {result3}")


# 脚本入口：仅在直接运行脚本时执行main函数
if __name__ == "__main__":
    main()
