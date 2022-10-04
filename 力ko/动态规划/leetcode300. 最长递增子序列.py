from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        # dp[i] 表示以nums[i] 结尾的最长递增子序列
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
        print(max(dp))
        return max(dp)


if __name__ == '__main__':
    s = Solution()
    data = [10, 9, 2, 5, 3, 7, 101, 18]
    data = [0, 1, 0, 3, 2, 3]
    data = [7, 7, 7, 7, 7, 7, 7]
    data = [5, 7, 1, 9, 4, 6, 2, 8, 3, 11]
    s.lengthOfLIS(data)
