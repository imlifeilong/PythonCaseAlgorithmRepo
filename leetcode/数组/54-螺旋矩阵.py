from typing import List

'''
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
'''


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # a 第一行 b 最后一行
        # c 第一列 d 最后一列
        a = c = 0
        b = len(matrix) - 1
        d = len(matrix[0]) - 1

        result = []
        while a <= b and c <= d:
            if a == b:
                for i in range(c, d + 1):
                    # print(matrix[a][i], end=',')
                    result.append(matrix[a][i])
            elif c == d:
                for i in range(a, b + 1):
                    result.append(matrix[i][c])
                    # print(matrix[i][c], end=',')
            else:
                # 第一行 从左到右
                for i in range(c, d):
                    result.append(matrix[a][i])

                # 最后一列 从上到下
                for i in range(a, b):
                    result.append(matrix[i][d])

                # 最后一行 从右到左
                for i in range(d, c, -1):
                    result.append(matrix[b][i])

                # 第一列 从下向上
                for i in range(b, a, -1):
                    result.append(matrix[i][c])

            a += 1
            b -= 1
            c += 1
            d -= 1

        print(result)
        return result


if __name__ == '__main__':
    # matrix = [
    #     [1, 2, 3, 4, 5],
    #     [6, 7, 8, 9, 10],
    #     [11, 12, 13, 14, 15]
    # ]
    matrix = [[3], [2]]
    # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s = Solution()
    s.spiralOrder(matrix)
