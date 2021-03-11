from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''滑动窗口'''
        length = len(nums)
        result = length + 1
        j = 0
        sums = 0
        for i in range(length):
            sums += nums[i]

            while sums >= target:
                min_length = i - j + 1
                result = result if result < min_length else min_length
                sums -= nums[j]
                j += 1

        return 0 if result == length + 1 else result

    def minSubArrayLen1(self, target: int, nums: List[int]) -> int:
        '''暴力循环'''
        length = len(nums)
        result = length + 1

        for i in range(length):
            sums = 0
            for j in range(i, length):
                sums += nums[j]
                if sums >= target:
                    # 计算最小序列长度
                    min_length = j - i + 1
                    result = result if result < min_length else min_length
                    break

        return 0 if result == length + 1 else result


if __name__ == '__main__':
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    s = Solution()
    res = s.minSubArrayLen(target, nums)
    print(res)
