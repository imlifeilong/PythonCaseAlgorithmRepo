from typing import List

'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例 1：

输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
示例 2：

输入：digits = ""
输出：[]
示例 3：

输入：digits = "2"
输出：["a","b","c"]
 


23
2 -> a b c
3 -> d e f
第一层选a 第二层分别可以选 d e f
第一层选b 第二层分别可以选 d e f
第一层选c 第二层分别可以选 d e f


(a)bc   (d)ef
        d(e)f
        de(f)

a(b)c   (d)ef
        d(e)f
        de(f)
        
ab(c)   (d)ef
        d(e)f
        de(f)
'''


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

    def letterCombinations(self, digits: str) -> List[str]:
        self.digits = digits
        self.length = len(self.digits)
        self.result = []
        self.backtrack(0, [])
        print(self.result)
        # self.dfs(0, digits, [])
        return self.result

    def backtrack(self, h, tmp):
        # h 表示要递归的层数 也就是最多达到 digits的长度
        # tmp 记录值的栈

        # 终止条件，就是当递归的次数达到 digits的长度时结束
        if h == self.length:
            self.result.append(''.join(tmp[:]))
            return
            # 遍历之前先找出 数字所代表的所有字母
        # self.digits[h] h从0开始 表示digits中第h个元素
        chars = self.mapping[self.digits[h]]

        # 因为每一层要遍历的元素都不一样，所以都需要从0位置开始，进行组合
        for i in range(len(chars)):
            tmp.append(chars[i])
            # 每层每次只添加一个元素 添加完后去下一层进行添加
            self.backtrack(h + 1, tmp)
            tmp.pop()


if __name__ == '__main__':
    digits = "23"
    digits = "2"
    s = Solution()
    s.letterCombinations(digits)
