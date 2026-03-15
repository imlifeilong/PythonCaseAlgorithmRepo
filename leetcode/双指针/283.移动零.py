# 导入列表类型注解，用于指定函数参数的类型
from typing import List


# 定义解决方案类，包含两种移动零的实现方法
class Solution:
    """
    包含两种移动零算法的类：
    1. moveZeroes_brute: 暴力解法，时间复杂度O(n²)
    2. moveZeroes: 双指针最优解法，时间复杂度O(n)
    """

    def moveZeroes_brute(self, nums: List[int]) -> None:
        """
        暴力解法：将非零元素向前移动，末尾补零（直接修改原数组，无返回值）
        :param nums: 包含零元素的整数列表，需要将所有零移动到末尾且保持非零元素相对顺序
        """
        # 获取数组长度
        n = len(nums)
        # 遍历指针，用于逐个检查数组元素
        i = 0
        # 记录已处理（已移动到末尾）的零的个数，用于缩小后续遍历范围
        processed = 0  # 已处理的元素个数

        # 遍历数组：由于每处理一个零，末尾就会固定一个零，因此只需遍历到 n - processed 位置
        while i < n - processed:
            # 如果当前元素是零，需要进行处理
            if nums[i] == 0:
                # 将当前零后面的所有非零元素向前移动一位（覆盖当前零的位置）
                for j in range(i + 1, n - processed):
                    nums[j - 1] = nums[j]
                # 在当前未处理部分的末尾补零（完成一个零的移动）
                nums[n - processed - 1] = 0
                # 已处理的零个数加一，后续遍历范围缩小
                processed += 1  # 增加已处理的0的个数
            else:
                # 如果当前元素不是零，直接移动遍历指针，检查下一个元素
                i += 1  # 只有当前元素不是0时才移动指针

    def moveZeroes(self, nums: List[int]) -> None:
        """
        双指针最优解法：将非零元素交换到前面，零自然留在末尾（直接修改原数组，无返回值）
        :param nums: 包含零元素的整数列表，需要将所有零移动到末尾且保持非零元素相对顺序
        """
        # 获取数组长度
        n = len(nums)
        # 左指针（慢指针）：记录下一个非零元素应该放置的位置，初始化为0
        # 右指针（快指针）：用于遍历数组，寻找非零元素，初始化为0
        left = right = 0

        # 遍历数组：右指针逐个遍历所有元素，直到数组末尾
        while right < n:
            # 如果右指针指向的元素不为零，说明需要将其放到左指针的位置
            if nums[right] != 0:
                # 交换左右指针指向的元素：将非零元素移到左指针位置，零移到右指针位置
                nums[left], nums[right] = nums[right], nums[left]
                # 左指针右移一位，准备接收下一个非零元素
                left += 1  # 左指针右移
            # 无论当前元素是否为零，右指针始终右移，继续遍历下一个元素
            right += 1  # 右指针始终右移


# 主程序入口，用于测试两种移动零的方法
if __name__ == "__main__":
    # 创建Solution类的实例
    solution = Solution()
    # 定义测试数组：需要将零移动到末尾的示例数组
    nums = [0, 1, 0, 3, 12]

    # 打印原数组，用于对比
    print(f"原数组: {nums}")

    # 先调用暴力解法处理数组（处理后数组已满足要求）
    solution.moveZeroes_brute(nums)
    # 再调用双指针解法处理数组（对已排好的数组无影响，仅作演示）
    solution.moveZeroes(nums)

    # 打印处理后的数组，查看结果
    print(f"移动零后: {nums}")
