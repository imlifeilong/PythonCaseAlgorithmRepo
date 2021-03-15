from typing import List

'''
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]

输入：n = 1
输出：[[1]]


'''


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # a 第一行 b 最后一行
        # c 第一列 d 最后一列
        mid = n // 2
        a = c = 0
        b = d = n
        index = 1
        # matrix = [[0] * n] * n  # 有问题 将一维数组赋值n次 只要其中一个改变，其他n-1个也会随之变化
        # 正确做法
        matrix = [[0] * n for _ in range(n)]

        while a < n and c < n:
            # 最上列，从左到右，左闭右开
            for i in range(c, d - 1):
                matrix[a][i] = index
                index += 1

            # 最后一列，从上向下
            for i in range(a, b - 1):
                matrix[i][d - 1] = index
                index += 1

            # 最后一行，从右向左
            for i in range(d - 1, c, -1):
                matrix[b - 1][i] = index
                index += 1

            # 第一列，从下向上
            for i in range(b - 1, a, -1):
                matrix[i][c] = index
                index += 1

            # 最外面循环完， 左上点 向右下移动
            a += 1
            b -= 1
            # 右下点，向左上移动
            c += 1
            d -= 1
        # 奇数情况，处理中心位置
        if n % 2:
            matrix[mid][mid] = index
        return matrix


if __name__ == '__main__':
    s = Solution()
    s.generateMatrix(6)
