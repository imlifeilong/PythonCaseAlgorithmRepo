from typing import List
import copy


class Solution:
    def subsets(self, nums):
        if not nums:
            return []

        def dfs(start_index, nums, res, path):
            res.append(path[:])
            for i in range(start_index, len(nums)):
                print(nums[i])
                # 1.设置现场
                path.append(nums[i])
                # 2.递归
                dfs(i + 1, nums, res, path)
                # 3.恢复现场
                path.pop()

        res = []
        path = []
        start_index = 0
        dfs(start_index, nums, res, path)
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    s = Solution()
    res = s.subsets(nums)
    print(res)
