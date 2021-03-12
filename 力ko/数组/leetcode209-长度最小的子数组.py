from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''滑动窗口
        窗口里面就是满足和小于等于目标值的最小长度的子数组
        尾指针 从开始位置遍历整个数组
        头指针 当窗口里的和大于等于目标值，头指针开始移动，直到不满足停止
        '''
        length = len(nums)
        result = length + 1
        j = 0
        sums = 0
        for i in range(length):
            sums += nums[i]
            # 后指针开始移动 计算两个指针之间的和，直到和大于等于目标值后指针停止
            # 然后再移动前指针，再计算和，直到和大于等于目标值，记录长度，再移动后指针
            while sums >= target:
                min_length = i - j + 1
                result = result if result < min_length else min_length
                # 移动头指针
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
