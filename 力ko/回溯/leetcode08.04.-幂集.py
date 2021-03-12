from typing import List

'''
幂集。编写一种方法，返回某集合的所有子集。集合中不包含重复的元素。

说明：解集不能包含重复的子集。

示例:

 输入： nums = [1,2,3]
 输出：
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

'''


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
