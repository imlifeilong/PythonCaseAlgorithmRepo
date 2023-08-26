class Solution:
    def countSubIslands(self, grid1, grid2):
        """

        思路
        1、找到g2中的子岛，并且在找的过程中，判断 g2是连续的岛的位置 在g1中对应的位置是否为0，如果是0就说明不是子岛
        2、统计子岛数量
        """

        def dfs(i, j):
            # dfs 表示 找到以i,j为开始的，所有相连的并且值为1的位置

            # 在g2中是岛，但在g1中不是岛，就判定为不是子岛
            # 在这个过程中，只要有一个位置不是岛屿，就标记为不是子岛
            if grid2[i][j] == 1 and grid1[i][j] == 0:
                nonlocal issublands
                issublands = False

            # 为了防止重复，将访问过的位置用不同的值标记
            grid1[i][j] = 2
            grid2[i][j] = 2

            # 试探 上下左右 四个方向
            for x0, y0 in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x, y = x0 + i, y0 + j

                # 这四个点 不越界，并且值为1的时候，再递归的去试探它的四个方向
                if 0 <= x < m and 0 <= y < n and grid2[x][y] == 1:
                    dfs(x, y)

        m = len(grid1)
        n = len(grid1[0])

        count = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    issublands = True
                    dfs(i, j)
                    # 如果是子岛，数量加1
                    if issublands:
                        count += 1

        return count


if __name__ == '__main__':
    grid1 = [[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]]
    grid2 = [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]

    grid1 = [[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1]]
    grid2 = [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]]
    s = Solution()
    res = s.countSubIslands(grid1, grid2)
    print(res)
