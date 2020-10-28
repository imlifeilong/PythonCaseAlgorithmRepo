from typing import List


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
