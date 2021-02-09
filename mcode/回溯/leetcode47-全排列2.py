from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 先排序，让重复的数在一块
        self.nums = sorted(nums)
        self.result = []
        self.flags = [0 for i in self.nums]

        self.dfs([])

        print(self.result)

    def dfs(self, tmp):
        if len(tmp) == len(self.nums):
            self.result.append(tmp.copy())
            return

        for i in range(len(self.nums)):
            # 如果当前位置被标记过，说明该元素已经用过
            if self.flags[i] == 1:
                continue

            print(i, self.flags)
            # 当前元素和上一个元素相同，并且上一个元素没有被标记
            if i > 0 and self.nums[i] == self.nums[i - 1] and self.flags[i - 1] == 0:
                continue
            self.flags[i] = 1
            tmp.append(self.nums[i])
            self.dfs(tmp)
            tmp.pop()

            self.flags[i] = 0


if __name__ == '__main__':
    nums = [1, 1, 3]
    s = Solution()
    s.subsets(nums)
