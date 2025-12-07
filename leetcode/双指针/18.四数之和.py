from typing import List


class Solution:
    def fourSum_brute(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)  # 获取输入数组的长度
        # 边界条件：数组元素个数小于4时，不可能存在四元组，直接返回空列表
        if n < 4:
            return []

        nums.sort()  # 关键步骤1：排序（作用：1. 便于去重；2. 为后续优化打基础）
        result = []  # 存储最终符合条件的不重复四元组

        # 关键步骤2：四层循环枚举所有可能的四元组（a < b < c < d，保证索引递增避免重复组合）
        # 第一层循环：枚举第一个元素的索引a，范围[0, n-4]（后续需留3个元素给b、c、d）
        for a in range(n - 3):
            # 去重逻辑1：跳过与前一个元素相同的nums[a]，避免重复四元组
            # a > 0 确保不越界，nums[a] == nums[a-1] 表示当前元素与前一个重复
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            # 第二层循环：枚举第二个元素的索引b，范围[a+1, n-3]（后续需留2个元素给c、d）
            for b in range(a + 1, n - 2):
                # 去重逻辑2：跳过与前一个元素相同的nums[b]，注意b需大于a+1（避免跳过第一个合法b值）
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue
                # 第三层循环：枚举第三个元素的索引c，范围[b+1, n-2]（后续需留1个元素给d）
                for c in range(b + 1, n - 1):
                    # 去重逻辑3：跳过与前一个元素相同的nums[c]，注意c需大于b+1
                    if c > b + 1 and nums[c] == nums[c - 1]:
                        continue
                    # 第四层循环：枚举第四个元素的索引d，范围[c+1, n-1]
                    for d in range(c + 1, n):
                        # 去重逻辑4：跳过与前一个元素相同的nums[d]，注意d需大于c+1
                        if d > c + 1 and nums[d] == nums[d - 1]:
                            continue
                        # 核心判断：四数之和是否等于目标值target
                        # Python中int类型支持大数，无需担心溢出问题（与C++不同）
                        if nums[a] + nums[b] + nums[c] + nums[d] == target:
                            # 符合条件的四元组加入结果列表
                            result.append([nums[a], nums[b], nums[c], nums[d]])
        return result  # 返回所有不重复的四元组结果

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        找出所有和为target的不重复四元组（双指针优化版）

        参数:
        nums: List[int] - 输入整数数组
        target: int - 四数之和的目标值

        返回:
        List[List[int]] - 所有满足条件且不重复的四元组
        """
        # 1. 排序：核心前置操作，为去重、剪枝、双指针移动提供基础
        nums.sort()
        n = len(nums)  # 获取数组长度
        result = []    # 存储最终符合条件的四元组

        # 2. 第一层循环：枚举第一个数的索引i，范围[0, n-4]（需留3个位置给j、left、right）
        for i in range(n - 3):
            # 去重逻辑1：跳过与前一个元素重复的nums[i]，避免生成重复四元组
            # i > 0 确保不越界，nums[i] == nums[i-1] 表示当前元素与前一个重复
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 剪枝逻辑1：提前终止无效循环（优化性能）
            # 情况1：当前i开头的最小四数和 > target，后续更大的数也不可能满足，直接break
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            # 情况2：当前i开头的最大四数和 < target，当前i不可能满足，直接跳过该i，进入下一轮
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue

            # 3. 第二层循环：枚举第二个数的索引j，范围[i+1, n-2]（需留2个位置给left、right）
            for j in range(i + 1, n - 2):
                # 去重逻辑2：跳过与前一个元素重复的nums[j]，注意j > i+1避免跳过第一个合法j
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # 剪枝逻辑2：同理i的剪枝，进一步缩小无效循环范围
                # 情况1：当前i、j开头的最小四数和 > target，break当前j循环
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                # 情况2：当前i、j开头的最大四数和 < target，跳过该j，进入下一轮
                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                    continue

                # 4. 双指针优化：用left/right代替原本的第三、四层循环，将时间复杂度从O(n^4)降至O(n^3)
                left = j + 1  # 左指针：指向j的下一个元素（第三个数）
                right = n - 1 # 右指针：指向数组末尾（第四个数）

                # 双指针循环：left < right 保证指针不重叠，避免重复组合
                while left < right:
                    # 计算当前四数之和
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    # 5. 核心判断：根据四数和与target的关系调整指针
                    if total == target:
                        # 找到符合条件的四元组，加入结果集
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        # 去重逻辑3：跳过left指针重复的元素（避免重复四元组）
                        # left < right 防止指针越界，nums[left] == nums[left+1] 表示当前元素与下一个重复
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # 去重逻辑4：跳过right指针重复的元素
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        # 指针同时移动：寻找下一组可能的组合
                        left += 1
                        right -= 1

                    elif total < target:
                        # 四数和偏小，需要增大和，左指针右移（数组已排序，右移数值变大）
                        left += 1
                    else:
                        # 四数和偏大，需要减小和，右指针左移（数组已排序，左移数值变小）
                        right -= 1

        # 返回所有不重复的四元组结果
        return result


# 测试示例
if __name__ == "__main__":
    # 测试用例1
    nums1 = [1, 0, -1, 0, -2, 2]
    target1 = 0
    s = Solution()
    print(f"输入: nums = {nums1}, target = {target1}")
    print(f"输出: {s.fourSum(nums1, target1)}")
    print(f"输出: {s.fourSum_brute(nums1, target1)}")
    # 输出: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

    # 测试用例2
    nums2 = [2, 2, 2, 2, 2]
    target2 = 8
    print(f"输入: nums = {nums2}, target = {target2}")
    print(f"输出: {s.fourSum(nums2, target2)}")
    print(f"输出: {s.fourSum_brute(nums2, target2)}")
    # 输出: [[2, 2, 2, 2]]

    # 测试用例3（处理大数情况）
    nums3 = [1000000000, 1000000000, 1000000000, 1000000000]
    target3 = 0
    print(f"输入: nums = {nums3}, target = {target3}")
    print(f"输出: {s.fourSum(nums3, target3)}")
    print(f"输出: {s.fourSum_brute(nums3, target3)}")
    # 输出: []
