from typing import List

'''
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        self.result = []
        self.tmp = []

        self.dfs(1, n, k)

        print(self.result)

    def dfs(self, index, n, k):
        if len(self.tmp) == k:
            self.result.append(self.tmp.copy())
            return

        for i in range(index, n + 1):

            self.tmp.append(i)
            print(i, index, self.tmp)
            self.dfs(i + 1, n, k)
            self.tmp.pop()
        print('循环结束')


if __name__ == '__main__':
    n, k = 4, 3
    s = Solution()
    s.combine(n, k)
