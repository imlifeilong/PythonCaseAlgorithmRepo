from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.length = len(self.nums)
        self.result = []
        # self.process(0, [])
        # # 用字典去重，key为值，value为值对应的位置
        # self.position = {}
        self.backtrack(0, [])

        print(self.result)
        return self.result

    def backtrack(self, start, tmp):
        # 当扫完整个序列时，根据题意，子序列至少两个元素 记录一次，不需要终止递归
        if len(tmp) >= 2:
            self.result.append(tmp[:])

        # 定义在递归里 是为了去重同层的相同元素
        cache = {}
        for i in range(start, self.length):

            # 判断条件 当栈顶的元素比当前元素小的时候，把当前的元素加入栈顶
            if tmp and tmp[-1] > self.nums[i]:
                continue
            # 同层里如果有元素已经在cache中的 就跳过
            # 不同层 的元素是可以重复的
            if cache.get(self.nums[i], None):
                continue

            tmp.append(self.nums[i])
            cache[self.nums[i]] = True
            # 当前元素入栈后，去下一层时 要从下一位开始扫描
            self.backtrack(i + 1, tmp)
            tmp.pop()


if __name__ == '__main__':
    s = Solution()
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    nums = [4, 6, 7, 7]
    s.findSubsequences(nums)
