class Solution:
    def closedIsland(self, grid):
        def dfs(i, j):
            # 如果相连的岛中有一个到达的边界，就返回False
            # m是岛的宽度，所以最后一个位置的索引是 m-1 ，n-1也是同理
            if i <= 0 or i >= m - 1:
                return False
            if j <= 0 or j >= n - 1:
                return False
            # 访问过的标记为2
            grid[i][j] = 2

            tmp = True

            for x0, y0 in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x, y = x0 + i, y0 + j

                # 这四个点 不越界，并且值为1的时候，再递归的去试探它的四个方向
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 0:
                    # & 使用与操作是因为，所有的岛都要求没在边界上
                    tmp &= dfs(x, y)

            return tmp

        """
        思路
        1、遍历找到所有的0
        2、使用dfs找到所有相连的岛，如果其中相连岛 到达边界了，就不是封闭的
        3、如果是封闭的岛 就统计
        """
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if dfs(i, j):
                        count += 1

        return count


if __name__ == '__main__':
    grid = [
        [1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 0],
        [1, 0, 1, 0, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0]
    ]
    grid = [[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]
    grid = [[1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1]]
    s = Solution()
    res = s.closedIsland(grid)
    print(res)
