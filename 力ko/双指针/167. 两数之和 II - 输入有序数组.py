"""
输入：numbers = [2,7,11,15], target = 9
输出：[1,2]
解释：2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。返回 [1, 2] 。

输入：numbers = [2,3,4], target = 6
输出：[1,3]
解释：2 与 4 之和等于目标数 6 。因此 index1 = 1, index2 = 3 。返回 [1, 3] 。

输入：numbers = [-1,0], target = -1
输出：[1,2]
解释：-1 与 0 之和等于目标数 -1 。因此 index1 = 1, index2 = 2 。返回 [1, 2] 。
"""


class Solution:
    def twoSum(self, numbers, target):
        # 暴力解决 复杂度 O(N^2)
        indexs = [-1, -1]
        n = len(numbers)
        for i in range(n):
            for j in range(i + 1, n):
                if numbers[i] + numbers[j] == target:
                    indexs = [i + 1, j + 1]
                    break
        print(indexs)
        return indexs

    def double_points(self, numbers, target):
        # 双指针 复杂度 O(N) 空间复杂度为 O(1)
        left = 0
        right = len(numbers) - 1
        indexs = [-1, -1]
        while left < right:
            sumval = numbers[left] + numbers[right]
            if sumval == target:
                indexs = [left + 1, right + 1]
                break
            elif sumval > target:
                right -= 1
            else:
                left += 1
                right -= 1
        print(indexs)
        return indexs


if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9

    numbers = [2, 3, 4]
    target = 6

    numbers = [-1, 0]
    target = -1

    s = Solution()
    s.twoSum(numbers, target)
    s.double_points(numbers, target)
