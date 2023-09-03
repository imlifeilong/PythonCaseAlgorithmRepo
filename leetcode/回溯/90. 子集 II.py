class Solution:
    def subsetsWithDup(self, nums):
        # 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列
        self.nums = nums
        self.length = len(self.nums)
        self.result = []
        self.backtrack(0, [])
        print(self.result)
        return self.result

    def backtrack(self, start, tmp):

        # 不需要终止，记录所有的
        self.result.append(tmp[:])

        # 使用字典进行同层数据去重
        cache = {}
        #
        for i in range(start, self.length):

            # 如果同层中有相同的数据就跳过
            if cache.get(self.nums[i], None):
                continue

            tmp.append(self.nums[i])
            cache[self.nums[i]] = True

            # 下一层中可以有重复的数据
            self.backtrack(i + 1, tmp)
            tmp.pop()


class Solutions:
    def subsetsWithDup(self, nums):
        # 使用排序进行去重
        self.nums = sorted(nums)
        self.length = len(self.nums)
        self.result = []
        self.backtrack(0, [])
        print(self.result)
        return self.result

    def backtrack(self, start, tmp):

        # 不需要终止，记录所有的
        self.result.append(tmp[:])

        for i in range(start, self.length):

            # 同层元素去重，当前元素与强一个元素相同，并且前一个元素已经添加过了，就跳过
            if i > start and self.nums[i] == self.nums[i - 1]:
                continue

            tmp.append(self.nums[i])
            # 下一层中可以有重复的数据
            self.backtrack(i + 1, tmp)
            tmp.pop()


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 2]
    # nums = [0]
    # s.subsetsWithDup(nums)

    obj = Solutions()
    obj.subsetsWithDup(nums)
