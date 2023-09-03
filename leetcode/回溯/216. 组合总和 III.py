"""
找出所有相加之和为 n 的 k 个数的组合，且满足下列条件：

只使用数字1到9
每个数字 最多使用一次
返回 所有可能的有效组合的列表 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。

示例 1:

输入: k = 3, n = 7
输出: [[1,2,4]]
解释:
1 + 2 + 4 = 7
没有其他符合的组合了。
示例 2:

输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]
解释:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
没有其他符合的组合了。
示例 3:

输入: k = 4, n = 1
输出: []
解释: 不存在有效的组合。
在[1,9]范围内使用4个不同的数字，我们可以得到的最小和是1+2+3+4 = 10，因为10 > 1，没有有效的组合。

"""


class Solution:
    def combinationSum3(self, k, n):
        self.k = k
        self.n = n
        self.result = []
        self.backtrack(1, 0, [], self.n)
        print(self.result)
        return self.result

    def backtrack(self, start, h, tmp, n):
        # start 每次遍历的开始位置
        # h 递归的层数 即也是tmp中元素的个数 当h超过 k时 就要终止了
        # tmp 记录 栈
        # n 目标值，当目标值为0 并且 tmp中的元素格式刚好是k个时 就记录tmp并终止递归

        # 剪枝层数大于 k时终止递归
        if h > self.k:
            return

        # 符合条件时 终止递归 并记录tmp
        if n == 0 and h == self.k:
            self.result.append(tmp[:])
            return

        # 因为每个元素只用一次，所以每次遍历都时要有开始位置
        for x in range(start, 10):

            # 当前值 小于或等于目标值时，继续递归试探
            if n >= x:
                tmp.append(x)
                # 每个元素只能使用一次，所以当前元素使用完后，只能使用后面的元素，所以下一层遍历的开始位置是 i+1
                # 去下一层递归的深度加1，目标值减去当前值
                self.backtrack(x + 1, h + 1, tmp, n - x)
                tmp.pop()


if __name__ == '__main__':
    k = 3
    n = 7
    # k = 3
    # n = 9
    k = 4
    n = 1

    k = 4
    n = 20
    s = Solution()
    s.combinationSum3(k, n)
