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
        self.length = len(nums)
        self.nums = nums

        self.result = []

        self.backtrack([])

        print(self.result)

    def backtrack(self, tmp):
        # tmp 记录符合的集合
        if len(tmp) == self.length:
            self.result.append(tmp.copy())
            return

        # 因为 全排列 元素可以重复使用，所以每次遍历都是从头开始
        for i in range(len(self.nums)):
            # in 时间复杂度O(N)
            # 因为序列是不重复的，所以如果当前的元素已经再集合中，就跳过
            if self.nums[i] in tmp:
                continue

            # 添加当前的元素
            tmp.append(self.nums[i])
            self.backtrack(tmp)
            tmp.pop()


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.length = len(nums)
        self.nums = nums

        self.result = []

        # self.backtrack([])

        self.position = []
        self.backtrack_p([])

        print(self.result)

    def backtrack(self, tmp):
        # tmp 记录符合的集合
        if len(tmp) == len(self.nums):
            self.result.append(tmp.copy())
            return

        # 因为 全排列 元素可以重复使用，所以每次遍历都是从头开始
        for i in range(len(self.nums)):
            # in 时间复杂度O(N)
            # 因为序列是不重复的，所以如果当前的元素已经再集合中，就跳过
            if self.nums[i] in tmp:
                continue

            # 添加当前的元素
            tmp.append(self.nums[i])
            self.backtrack(tmp)
            tmp.pop()

    def backtrack_p(self, tmp):
        # 终止条件 就是元素个数 已经达到原来序列的长度，就可以退出
        # 递归就是递归深度，如果不限制就一直遍历下去，可能元素个数就会是 4个 5个 100个。。。
        if len(tmp) == self.length:
            # 当已经记录和原来序列长度相同的元素时
            self.result.append(tmp[:])
            return

        for i in range(self.length):
            # 如果元素的索引已经被访问过，就跳过
            if i in self.position:
                continue
            # 记录元素的索引 是否已经访问过
            self.position.append(i)

            # 记录元素
            tmp.append(self.nums[i])
            self.backtrack_p(tmp)
            # 回溯
            tmp.pop()
            self.position.pop()


if __name__ == '__main__':
    nums = [1, 2, 3]
    s = Solution()
    s.subsets(nums)
