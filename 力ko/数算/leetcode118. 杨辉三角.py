"""
给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。

输入: numRows = 5
输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        return self.process(numRows)

    def process(self, length):
        result = []
        for row in range(length):
            temp = []
            for i in range(row + 1):
                if i == 0 or i == row:
                    temp.append(1)
                else:
                    t = result[row - 1][i - 1] + result[row - 1][i]
                    temp.append(t)
            result.append(temp)
        print(result)
        return result


if __name__ == '__main__':
    s = Solution()
    s.generate(3)
