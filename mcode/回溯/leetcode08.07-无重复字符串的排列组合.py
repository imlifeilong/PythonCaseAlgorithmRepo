from typing import List


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
