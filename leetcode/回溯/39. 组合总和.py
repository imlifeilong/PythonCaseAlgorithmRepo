"""
示例 1：

输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
解释：
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
7 也是一个候选， 7 = 7 。
仅有这两种组合。
示例 2：

输入: candidates = [2,3,5], target = 8
输出: [[2,2,2,2],[2,3,3],[3,5]]
示例 3：

输入: candidates = [2], target = 1
输出: []

2 3 6 7
7

要求 每一个组合中的元素时可以重复的，但是不能有重复的组合
每次选择一个元素后，去下一层遍历的时候，就不能再选这个元素了


第1层选2 第2层可以继续选2 第3层还能选2 第4层的时候 2+2+2+2=8 大于 目标值7了 不符合所以跳过，
                                   第4层选 3 6 7 的时候结果都是大于7的 都不符合
2 2 2 2
2 2 2 3
2 2 2 6
2 2 2 7

第4层的时候所有的元素都不符合，所以回溯到第3层
第3层选3 刚好 2+2+3=7满足条件 记录下来
第3层选6 7 都大于7 不符合

2 2 3   #
2 2 6
2 2 7

回溯到第2层 2的所有情况已经完了，所以接下来从3开始，
此时第3层的 选择2 和组合结果 2 2 3 重复了，不能记录，
这种处理办法就是，在去下一层的时候，只能从当前的元素开始，不能取前面的，所以每次遍历的时候就给 一个初始位置
2 3 2   # 重复了
2 3 3
2 3 6
2 3 7

2 6
2 7


3 2 2   # 重复了
3 2 3
3 2 6
3 2 7

3 3 2
3 3 3
3 3 6
3 3 7

3 6
3 7

6 3
6 7

7       #


"""


class Solution:
    def combinationSum(self, candidates, target):
        self.candidates = candidates
        self.target = target
        self.length = len(self.candidates)
        self.reault = []
        # self.position = [False] * self.length
        self.backtrack(0, [], self.target)
        print(self.reault)
        return self.reault

    def backtrack(self, start, tmp, target):
        # start  表示每层遍历的开始位置
        # tmp 存元素的临时栈，每递归一层 就入栈一个元素，递归完成后，则弹出栈顶元素 可以实现回溯
        # target 目标值，为0时就达到目的，结束递归

        # 终止条件 当目标值为0的时候，就终止递归
        if target == 0:
            self.reault.append(tmp[:])
            return
        # 在每一层用过的元素就不会再用了，所以需要记录下每层的开始位置
        for i in range(start, self.length):

            # 因为每个元素可以重复使用，所以对于各元素来说，不需要去重
            # 但是需要满足条件，就是当前所选的值，一定要小于等于目标时，才能选择，并去下一层再试探
            if target >= self.candidates[i]:
                tmp.append(self.candidates[i])
                # 在不同层中，可以使用相同的元素，所以使用i 说明在下一层试探的时候，还可以选择当前的元素
                # start 表示在同一层遍历的时候的开始位置，i表示在下一层开始位置
                self.backtrack(i, tmp, target - self.candidates[i])
                tmp.pop()


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    candidates = [2, 3, 5]
    target = 8
    s = Solution()
    s.combinationSum(candidates, target)
