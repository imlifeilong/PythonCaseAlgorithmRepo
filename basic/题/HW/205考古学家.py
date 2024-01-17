from typing import List


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
            # 去掉重复的结果
            row = ''.join(tmp[:])
            if row not in self.result:
                self.result.append(row)
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
    nums = ['a', 'b', 'c']
    s = Solution()
    res = s.subsets(nums)
    for row in res:
        print(''.join(row))
