from typing import List

'''
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

组合是指从一组元素中选择若干个元素，不考虑元素的顺序，而只考虑元素的组合方式。组合通常用于解决从给定集合中选择子集的问题
组合数 指的是不考虑元素顺序的情况下，从元素集合中选择指定数量的元素的方式的总数。
排列数 与组合不同，排列考虑元素的顺序，因此同样的元素可以以不同的顺序组成不同的排列

从 [1,2,3,4] 中选择2个数 进行组合
第一层选择1 第二层可以从剩下的 2 3 4 中选择 第二层选择的范围是[1,n) 索引位置是从0开始的 
第一层选择2 第二层可以选择 3 4      选择范围是[2,n)
第一层选择3 第二层可以选择 4        选择范围[3,n)
第一层选择4 第二层没有可选的元素     选择范围是[4,n)  

(1)234  (12)34
        (13)24
        (14)23

1(2)34  1(23)4
        1(24)3

12(3)4  12(34)

123(4)
'''


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.result = []
        self.n = n
        self.k = k
        
        # 生成1-n的序列
        self.nums = list(range(1, self.n + 1))
        self.backtrack(0, 0, [])
        print(self.result)
        return self.result

    def backtrack(self, start, h, tmp):
        # start 每层遍历时开始的位置
        # h     递归的层数，因为每一层只记录1个数 当层数达到k时 就达到终止条件
        # tmp   记录结果的栈 每一层只入栈1个元素

        if h == self.k:
            self.result.append(tmp[:])
            return

        for i in range(start, self.n):
            tmp.append(self.nums[i])
            # 去下一层试探，i+1表示下一层 是从当前元素的下一位开始遍历的， h+1表示 层数加1
            self.backtrack(i + 1, h + 1, tmp)
            tmp.pop()


if __name__ == '__main__':
    n, k = 4, 2
    n, k = 1, 1
    s = Solution()
    s.combine(n, k)
