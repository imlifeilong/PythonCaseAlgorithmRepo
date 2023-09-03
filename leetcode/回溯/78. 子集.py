"""
示例 1：

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
示例 2：

输入：nums = [0]
输出：[[],[0]]

123为例
第一层选择1  第二层选择可以选2或者3    第三层选剩下的元素，子集没有顺序 所以123和132是同一个子集
第一层选择2  第二层选择剩下的3
第一层选择3  没有剩余的元素然后退出

(1)23       (12)3       (123)
            (13)2
1(2)3       1(23)

12(3)

"""


class Solution:
    def subsets(self, nums):
        self.nums = nums
        self.length = len(self.nums)
        self.result = []
        self.backtrack(0, [])
        print(self.result)
        return self.result

    def backtrack(self, start, tmp):
        # 所有路径都应该加入结果集，所以不存在结束条件。
        # 或者说当 start 参数越过数组边界的时候，程序就自己跳过下一层递归了，因此不需要手写结束条件,直接加入结果集
        # 子集是记录所有路径上的节点，全排列是记录所有符合的叶节点
        self.result.append(tmp[:])
        # 子集 包含空集和本身 是无顺序的 [1,2]和[2,1]是同一个自己，所以要保证这两种结果只出现一次就行

        for i in range(start, self.length):
            # 因为结果中不能有重复值，所以需要记录开始位置
            tmp.append(self.nums[i])
            # 去下一层的时候，开始遍历的位置就是当前元素的下一位了，意思再从剩下的元素中选
            self.backtrack(i + 1, tmp)
            tmp.pop()


if __name__ == '__main__':
    nums = [1, 2, 3]
    # nums = [0]
    s = Solution()
    s.subsets(nums)
