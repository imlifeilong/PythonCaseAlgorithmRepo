from typing import List

'''
n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。

每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

 

示例 1：


输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如上图所示，4 皇后问题存在两个不同的解法。
示例 2：

输入：n = 1
输出：[["Q"]]
 

提示：

1 <= n <= 9
皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。

'''


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.index = 1
        self.n = n
        self.chessboard = [[0] * self.n for i in range(self.n)]
        # 列
        self.col = set()
        # 正对角线
        self.d1 = set()
        # 反对角线
        self.d2 = set()
        self.result = []
        self.dfs(0)

    def dfs(self, row):
        if row >= self.n:
            print(self.index, '----------------------')
            self.printq()
            self.index += 1
            self.result.append(self.chessboard)
            return self.result

        for col in range(self.n):
            # print(row, col, self.col)
            d1, d2 = col + row, col - row
            # 检查列是否被占用
            if col in self.col:
                continue
            # 检查正对角线是否被占用 列-行
            if d1 in self.d1:
                continue
            # 检查反对角线是否被占用 列+行
            if d2 in self.d2:
                continue

            # 放置皇后
            self.chessboard[row][col] = 1

            # 标记
            self.col.add(col)
            self.d1.add(d1)
            self.d2.add(d2)

            # 纵向遍历，检查下一行
            self.dfs(row + 1)

            # 回溯
            self.col.remove(col)
            self.d1.remove(d1)
            self.d2.remove(d2)
            self.chessboard[row][col] = 0

    def printq(self):
        for i in self.chessboard:
            x = []
            for j in i:
                x.append('0 ')
                if j == 1:
                    x.append('1 ')

            print(''.join(x))


if __name__ == '__main__':
    s = Solution()
    res = s.solveNQueens(8)
    print(res)
