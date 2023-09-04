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
        self.length = len(self.nums)
        self.position = [False] * self.length

        self.backtrack([])
        print(self.result)
        return self.result

    def backtrack(self, tmp):
        if len(tmp) == len(self.nums):
            self.result.append(tmp[:])
            return

        for i in range(len(self.nums)):
            # 当前元素与上一位元素相同，并且上一位元素已经用过了 就跳过， 层 去重复
            if i > 0 and self.nums[i] == self.nums[i - 1] and self.position[i - 1]:
                continue
            # 如果当前的元素已经用过了，就跳过 枝去重
            if self.position[i]:
                continue

            tmp.append(self.nums[i])
            self.position[i] = True
            self.backtrack(tmp)
            tmp.pop()
            self.position[i] = False


if __name__ == '__main__':
    nums = [1, 1, 2]
    s = Solution()
    s.subsets(nums)
