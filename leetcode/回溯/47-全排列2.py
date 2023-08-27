from typing import List

'''
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

 

示例 1：

输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]
示例 2：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

提示：

1 <= nums.length <= 8
-10 <= nums[i] <= 10

'''


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 先排序，让重复的数在一块
        self.nums = sorted(nums)
        self.result = []
        self.flags = [0 for i in self.nums]

        self.dfs([])

        print(self.result)
        return self.result

    def dfs(self, tmp):
        if len(tmp) == len(self.nums):
            self.result.append(tmp.copy())
            return

        for i in range(len(self.nums)):
            # 如果当前位置被标记过，说明该元素已经用过
            if self.flags[i] == 1:
                continue

            # print(i, self.flags)
            # 当前元素和上一个元素相同，并且上一个元素没有被标记
            if i > 0 and self.nums[i] == self.nums[i - 1] and self.flags[i - 1] == 0:
                continue
            self.flags[i] = 1
            tmp.append(self.nums[i])
            self.dfs(tmp)
            tmp.pop()

            self.flags[i] = 0


if __name__ == '__main__':
    nums = [1, 1, 3, 2]
    s = Solution()
    s.subsets(nums)
