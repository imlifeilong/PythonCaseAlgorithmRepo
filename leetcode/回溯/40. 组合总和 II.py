"""

示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
输出:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
输出:
[
[1,2,2],
[5]
]
10,1,2,7,6,1,5
8

如果不排序的情况

(10) > 8
1 2 7 > 8
1 2 6 > 8
1 2 1 5 > 8
1 2 5 = 8

1 7   = 8
1 6 1 = 8
1 1 5 遍历完成
1 5   遍历完成

2 7   > 8
2 6   = 8
2 1 5 = 8 重复了 去重的方法 就是将所有的子集排序后，再进行去重，这样是再将所有的接过遍历完成之后，才能去重，效率非常低
2 5


2 7 > 8
2 6 = 8
2


"""


class Solution:
    def combinationSum2(self, candidates, target):
        self.candidates = candidates
        # 先对所有元素进行排序，再递归过程中进行去重，如果相邻的两个值相同，并且前一个值已经选过了，就不会选
        self.candidates.sort()

        self.target = target
        self.length = len(self.candidates)

        self.cache = []
        self.result = []
        self.backtrack(0, [], self.target)
        print(self.result)
        return self.result

    def backtrack(self, start, tmp, target):
        # start 在当前层遍历的开始位置
        # tmp 记录临时值的栈
        # target 目标值，当目标值为0是 就可以终止递归

        # 当目标值为0的时候就终止递归，记录此时的组合
        if target == 0:
            self.result.append(tmp[:])
            return

        for i in range(start, self.length):

            # 在同一层遍历的时候，如果两个相邻的元素相同，就跳过 使用i-1就说明 上一个位置的值已经被选过了
            # i > start 因为要和前一个元素比较，所以i的值必须时大于start的，不然会越界
            if i > start and self.candidates[i] == self.candidates[i - 1]:
                continue

            # 如果当前值比目标值小 或者 相等的时候，才去递归下一层，不然直接跳过
            if target >= self.candidates[i]:
                tmp.append(self.candidates[i])
                # 集合中 每各元素只能添加一次，所以添加完当前的元素后，去下一层试探的时候只能从下一位开始遍历，所以下一层的开始位置就是i+1
                self.backtrack(i + 1, tmp, target - self.candidates[i])
                tmp.pop()


if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    # candidates = [2, 5, 2, 1, 2]
    # target = 5
    s = Solution()
    s.combinationSum2(candidates, target)
