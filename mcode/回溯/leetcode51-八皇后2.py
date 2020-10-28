from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.index = 1
        self.n = n
        self.chessboard = {}
        # 列
        columns = set()
        # 正对角线
        d1s = set()
        # 反对角线
        d2s = set()
        self.result = []
        self.dfs(0, d1s, d2s, columns)
        return self.result

    def dfs(self, row, d1s, d2s, cols):
        if row >= self.n:
            self.result.append(self.printq())
            self.index += 1
            return

        for col in range(self.n):
            # print(row, col, self.col)
            d1, d2 = col + row, col - row
            # 检查列是否被占用
            if col in cols:
                continue
            # 检查正对角线是否被占用 列-行
            if d1 in d1s:
                continue
            # 检查反对角线是否被占用 列+行
            if d2 in d2s:
                continue

            # 放置皇后
            self.chessboard[row] = col

            # 标记
            cols.add(col)
            d1s.add(d1)
            d2s.add(d2)

            # 纵向遍历，检查下一行
            self.dfs(row + 1, d1s, d2s, cols)

            # 回溯
            cols.remove(col)
            d1s.remove(d1)
            d2s.remove(d2)
            del self.chessboard[row]

    def printq(self):
        result = []
        for k, v in self.chessboard.items():
            x = []
            for i in range(self.n):
                if i == v:
                    x.append('Q')
                else:
                    x.append('.')
            result.append(''.join(x))
        return result


if __name__ == '__main__':
    s = Solution()
    res = s.solveNQueens(4)
    print(len(res), res)
