class Solution:
    def exist(self, board, word):
        def dfs(i, j, index):
            #
            tmpc = board[i][j]
            # 将当前的点标记为 访问过
            board[i][j] = '0'

            # 所有的字符都找到时，返回True
            if index == len(word):
                return True

            tmp = False
            # 去四个方向 进行搜索
            for x0, y0 in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x, y = x0 + i, y0 + j
                if 0 <= x < m and 0 <= y < n and board[x][y] == word[index]:
                    # 只要右一条路可以走通就可以，所以使用或
                    tmp |= dfs(x, y, index + 1)
            # 回溯，访问之后，恢复
            board[i][j] = tmpc
            return tmp

        m = len(board)
        n = len(board[0])

        res = False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    res |= dfs(i, j, 1)
                    if res:
                        break
        return res


if __name__ == '__main__':
    # board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    # word = "ABCCED"
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "SEE"

    # board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    # word = "ABCB"

    board = [["C", "A", "A"],
             ["A", "A", "A"],
             ["B", "C", "D"]]
    word = "AAB"
    s = Solution()
    res = s.exist(board, word)
    print(res)
