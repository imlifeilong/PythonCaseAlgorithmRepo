from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.nums = nums
        self.length = len(self.nums)
        self.maxlen = 1
        self.backtrack(0, [])
        print(self.maxlen)

        self.process()

        return self.maxlen

    def backtrack(self, start, tmp):
        # 回溯
        # start 表示本层开始遍历的位置
        # tmp 栈，符合条件的元素 入栈

        # 当扫描完整个序列时，终止递归
        if start == self.length:
            # 取当前栈的长度 与 原来记录的最大长度 较大的
            self.maxlen = max(self.maxlen, len(tmp))
            return

        for i in range(start, self.length):
            # 遍历元素，与栈顶元素比较，如果比栈顶元素大，就入栈
            if tmp and tmp[-1] >= self.nums[i]:
                continue
            tmp.append(self.nums[i])
            # 去下一层的时候，从下一位元素开始遍历
            self.backtrack(i + 1, tmp)
            tmp.pop()

    def process(self):
        # 动态规划解
        dp = [1] * self.length
        # dp[i] 表示以nums[i] 结尾的最长递增子序列
        for i in range(self.length):
            for j in range(i):
                if self.nums[j] < self.nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
        print(dp)
        return max(dp)


if __name__ == '__main__':
    s = Solution()
    # data = [10, 9, 2, 5, 3, 7, 101, 18]
    # data = [0, 1, 0, 3, 2, 3]
    # data = [7, 7, 7, 7, 7, 7, 7]
    data = [5, 7, 1, 9, 4, 6, 2, 8, 3, 11]
    s.lengthOfLIS(data)
