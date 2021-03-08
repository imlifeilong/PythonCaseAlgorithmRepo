from typing import List

'''
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]


'''


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.result = []
        self.flags = [0 for i in self.nums]
        # self.dfs([])

        self.dfs1([])

        print(self.result)

    def dfs(self, tmp):
        if len(tmp) == len(self.nums):
            self.result.append(tmp.copy())
            return

        for i in range(len(self.nums)):
            # in 时间复杂度O(N)
            if self.nums[i] in tmp: continue
            tmp.append(self.nums[i])
            self.dfs(tmp)
            tmp.pop()

    def dfs1(self, tmp):
        if len(tmp) == len(self.nums):
            self.result.append(tmp.copy())
            return

        for i in range(len(self.nums)):

            if self.nums[i] in tmp: continue

            if self.flags[i] == 1: continue

            self.flags[i] = 1
            tmp.append(self.nums[i])
            self.dfs(tmp)
            tmp.pop()

            self.flags[i] = 0


if __name__ == '__main__':
    nums = [1, 2, 3]
    s = Solution()
    s.subsets(nums)
