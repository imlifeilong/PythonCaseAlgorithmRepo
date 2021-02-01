from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.result = []
        self.dfs(0, [])

        print(self.result)

    def dfs(self, index, tmp):
        self.result.append(tmp.copy())
        for n in range(index, len(self.nums)):
            tmp.append(self.nums[n])
            # 从下一位置开始组合
            self.dfs(n + 1, tmp)
            tmp.pop()


if __name__ == '__main__':
    nums = [1, 2, 3]
    s = Solution()
    s.subsets(nums)
