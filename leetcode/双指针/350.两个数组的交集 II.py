# 从typing模块导入List类型，用于类型注解，明确函数参数和返回值的数组类型
from typing import List


# 解决方案类：实现两个数组交集 II 的两种解法（暴力解法 + 双指针解法）
class Solution:
    """
    用于求解两个数组交集 II 的类，提供暴力解法和高效的双指针解法
    交集要求保留重复元素，重复次数与两个数组中该元素的最小出现次数一致
    """

    def intersect_brute(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        暴力解法：遍历nums1每个元素，在nums2中查找未被使用的相同元素
        :param nums1: 第一个输入整数数组
        :param nums2: 第二个输入整数数组
        :return: 两个数组的交集列表，保留重复元素，顺序与nums1中匹配顺序一致
        """
        result = []  # 初始化空列表，用于存储最终交集结果
        # 创建与nums2长度一致的布尔列表，标记nums2对应索引元素是否已被匹配使用，初始值全为False
        used = [False] * len(nums2)

        # 外层循环：遍历nums1中的每一个元素，逐个寻找其在nums2中的匹配项
        for num1 in nums1:
            # 内层循环：遍历nums2的所有元素，查找与num1相等且未被使用的元素
            for i in range(len(nums2)):
                # 找到有效匹配：nums2[i]未被使用且与num1值相等
                if not used[i] and nums2[i] == num1:
                    result.append(num1)  # 将匹配成功的元素加入结果列表
                    used[i] = True  # 标记nums2[i]为已使用，避免重复匹配
                    break  # 找到当前num1的匹配项后，退出内层循环，处理nums1下一个元素

        return result  # 返回最终的交集结果

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        双指针解法：先对两个数组排序，再通过双指针高效匹配相同元素（官方推荐高效解法）
        :param nums1: 第一个输入整数数组
        :param nums2: 第二个输入整数数组
        :return: 两个数组的交集列表，保留重复元素，顺序为排序后的升序顺序
        """
        # 第一步：对两个数组进行升序排序，为双指针有序匹配奠定基础
        nums1.sort()
        nums2.sort()

        result = []  # 初始化空列表，用于存储最终交集结果
        i, j = 0, 0  # 初始化双指针：i指向nums1起始位置，j指向nums2起始位置

        # 循环条件：两个指针均未超出对应数组的长度，任一指针越界则停止遍历
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                # 情况1：两个指针指向的元素相等，说明找到交集元素
                result.append(nums1[i])  # 将相等元素加入结果列表
                i += 1  # 移动nums1指针，寻找下一个可能的匹配项
                j += 1  # 移动nums2指针，寻找下一个可能的匹配项
            elif nums1[i] < nums2[j]:
                # 情况2：nums1指针元素更小，移动nums1指针寻找更大的元素，尝试匹配nums2[j]
                i += 1
            else:
                # 情况3：nums2指针元素更小，移动nums2指针寻找更大的元素，尝试匹配nums1[i]
                j += 1

        return result  # 返回最终的交集结果


if __name__ == "__main__":
    """
    主程序入口：用于测试两种解法的功能正确性，包括常规场景和边界场景
    """
    # 测试1：暴力解法（原代码此处调用错误，已修正为intersect_brute）
    sol1 = Solution()
    nums1 = [1, 2, 2, 1]  # 测试用例1：包含重复元素的数组1
    nums2 = [2, 2]        # 测试用例1：包含重复元素的数组2
    result1 = sol1.intersect_brute(nums1, nums2)  # 调用暴力解法方法
    print(f"暴力解法结果: {result1}")  # 打印暴力解法的交集结果

    # 测试2：双指针解法
    sol2 = Solution()
    nums3 = [4, 9, 5]                 # 测试用例2：无重复元素的数组1
    nums4 = [9, 4, 9, 8, 4]           # 测试用例2：包含重复元素的数组2
    result2 = sol2.intersect(nums3, nums4)  # 调用双指针解法方法
    print(f"双指针解法结果: {result2}")  # 打印双指针解法的交集结果

    # 测试3：边界场景 - 其中一个数组为空数组
    nums5 = [1, 2, 3]  # 非空数组
    nums6 = []         # 空数组（边界条件）
    result3 = sol2.intersect_brute(nums5, nums6)  # 用暴力解法测试空数组场景
    print(f"空数组测试结果: {result3}")  # 打印空数组场景的交集结果（预期为空列表）