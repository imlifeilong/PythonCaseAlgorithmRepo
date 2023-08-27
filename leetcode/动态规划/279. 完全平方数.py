'''
输入：n = 12
输出：3
解释：12 = 4 + 4 + 4
'''


class Solution:
    def numSquares(self, n: int) -> int:
        res = self.process(1, n)
        print(res)

    def process(self, index, n):
        # 目标值为0时，已经被分配完
        if n == 0:
            return 0

        # 当前值平方大于目标值时，需要舍弃这个分支，返回无穷大（因为要取最小值）
        if index * index > n:
            return float('inf')
        # 选择当前值，选择后可以继续选择当前值， 目标值减去当前值
        p1 = self.process(index, n - index * index) + 1
        # 不选当前值，去下个位置
        p2 = self.process(index + 1, n)
        return min(p1, p2)


if __name__ == '__main__':
    s = Solution()
    n = 12
    n = 17
    s.numSquares(n)
