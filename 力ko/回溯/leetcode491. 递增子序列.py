from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.result = []
        self.process(0, [])

        print(self.result)
        return self.result

    def process(self, index, tmp):
        if len(tmp) > 1 and tmp not in self.result:
            self.result.append(tmp[:])
        for i in range(index, len(self.nums)):
            # 剪枝
            if tmp and tmp[-1] > self.nums[i]:
                continue
            tmp.append(self.nums[i])
            self.process(i + 1, tmp)
            tmp.pop()


if __name__ == '__main__':
    s = Solution()
    data = [10, 9, 2, 5, 3, 7, 101, 18]
    s.findSubsequences(data)
