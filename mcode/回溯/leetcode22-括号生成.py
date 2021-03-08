from typing import List

'''
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

 

示例 1：

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：

输入：n = 1
输出：["()"]
 

提示：

1 <= n <= 8

'''


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []
        self.dfs(0, 0, n, '')
        return self.result

    def dfs(self, left, right, n, s):
        if left == n and right == n:
            self.result.append(s)
            return
        # 左括号可以无限入
        if left < n:
            self.dfs(left + 1, right, n, s + '(')
        # 右括号要比左括号少的时候，才能入
        if right < left and right < n:
            self.dfs(left, right + 1, n, s + ')')


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(4))
