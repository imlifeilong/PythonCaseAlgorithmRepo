from typing import List

'''
无重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合，字符串每个字符均不相同。

示例1:

 输入：S = "qwe"
 输出：["qwe", "qew", "wqe", "weq", "ewq", "eqw"]
示例2:

 输入：S = "ab"
 输出：["ab", "ba"]
提示:

字符都是英文字母。
字符串长度在[1, 9]之间。
'''


class Solution:
    def permutation(self, S: str) -> List[str]:
        self.s = S
        # self.t = []
        self.result = []
        self.dfs(0, [])
        print(self.result)

    def dfs(self, index, tmp):
        if index == len(self.s):
            self.result.append(''.join(tmp.copy()))
            return

        for c in self.s:
            # self.t.append(c)
            if c in tmp: continue
            tmp.append(c)
            print(index, c, tmp)
            self.dfs(index + 1, tmp)
            tmp.pop()


if __name__ == '__main__':
    st = 'abc'
    s = Solution()
    s.permutation(st)
