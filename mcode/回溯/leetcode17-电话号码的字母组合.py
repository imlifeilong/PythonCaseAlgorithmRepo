from typing import List


class Solution:
    mapping = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    result = []

    def letterCombinations(self, digits: str) -> List[str]:
        self.dfs(0, digits, [])
        return self.result

    def dfs(self, index, digits, tmp):
        if index == len(digits):
            self.result.append(''.join(tmp))
            return self.result

        for c in self.mapping[digits[index]]:
            # print('------------->', tmp)
            tmp.append(c)
            self.dfs(index + 1, digits, tmp)
            tmp.pop()


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations('233'))
