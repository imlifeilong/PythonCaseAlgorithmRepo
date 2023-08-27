class Solution:
    def solve(self, board):
        def dfs(i, j):
            board[i][j] = 'Y'

            for x0, y0 in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x, y = x0 + i, y0 + j
                if 0 <= x < m and 0 <= y < n and board[x][y] == 'O':
                    dfs(x, y)

        m = len(board)
        n = len(board[0])

        """
        思路
        1、先找到所有与边界相连的 O，再用dfs找到与之相连的所有的O，则此块区域不是被包围的，记录为 Y
        2、找出所有剩余的O，这些就是被包围的O，用X替换，然后将所有的Y用O替换回去
        """
        for i in range(m):
            for j in range(n):
                if (i in (0, m - 1) or j in (0, n - 1)) and board[i][j] == 'O':
                    dfs(i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'Y':
                    board[i][j] = 'O'

        for line in board:
            print(line)


if __name__ == '__main__':
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]
    board = [
        ["O", "X", "X", "O", "X"],
        ["X", "O", "O", "X", "O"],
        ["X", "O", "X", "O", "X"],
        ["O", "X", "O", "O", "O"],
        ["X", "X", "O", "X", "O"]
    ]
    s = Solution()
    res = s.solve(board)
    print(res)
