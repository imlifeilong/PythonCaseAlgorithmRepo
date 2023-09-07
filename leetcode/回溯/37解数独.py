class Solution:
    def solveSudoku(self, board):
        self.board = board
        self.rows = len(self.board)
        self.cols = len(self.board[0])

        res = self.backtrack()
        print(res)

        print(self.board)
        return self.board

    def backtrack(self):
        for i in range(self.rows):
            for j in range(self.cols):
                # 遍历第i行第j列的不是数字的情况下，去试探哪个数字符合条件
                if self.board[i][j] != '.':
                    continue
                for x in range(1, 10):
                    # 分别检测 该数字在行 列 九宫格中是否重复，如果重复了就跳过
                    if not self.isok(i, j, str(x)):
                        continue

                    self.board[i][j] = str(x)
                    # 如果 这个数字在这个位置符合条件，就直接返回，返回到上一层后，继续去下一个位置试探
                    if self.backtrack():
                        return True

                    self.board[i][j] = '.'
                # 所有的数字都不符合，就回溯，该位置的值恢复为 . 然后再试其他数字
                return False
        # 找见所有的空格子，并且填充成功
        return True

    def isok(self, row, col, value):

        # 判断行是否有重复值
        for i in range(9):
            if self.board[row][i] == value:
                return False

        # 判断列是否有重复值
        for j in range(9):
            if self.board[j][col] == value:
                return False

        # 判断九宫格里是否重复
        # 根据 row 和 col 计算此时是在哪个九宫格
        # 九宫格行开始位置
        row_start = (row // 3) * 3
        # 列开始位置
        col_start = (col // 3) * 3

        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                if self.board[i][j] == value:
                    return False
        # 所有的条件都符合
        return True


if __name__ == '__main__':
    s = Solution()
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    s.solveSudoku(board)
