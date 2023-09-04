from typing import List

'''
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。

回文串 是正着读和反着读都一样的字符串。

 

示例 1：

输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]
示例 2：

输入：s = "a"
输出：[["a"]]
 


aab

遍历
第一层取一个元素
a a b
a ab
aa b
aab


'''


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.result = []
        self.s = s
        self.length = len(self.s)
        self.backtrack(0, [])
        #
        # self.dfs(s, [])
        return self.result

    def backtrack(self, start, tmp):
        # start 要截取的字符串的开始位置
        # tmp 临时栈 用于存放元素

        # start == length表示扫描到字符串末尾了，后面没有字符了，就终止递归
        if start == self.length:
            self.result.append(tmp[:])
            return

        # 因为每次遍历的时候，开始的位置不同，所以要给定开始位置
        for i in range(start, self.length):
            # 截取字符串
            tmpstr = self.s[start:i + 1]
            # 判断是否时回文串
            if self.is_palindrome(tmpstr):
                tmp.append(tmpstr)
                # 去下一层遍历的时候，从当前位置的下一位开始，并且递归的深度加1
                self.backtrack(i + 1, tmp)
                tmp.pop()

    def is_palindrome(self, string):
        # 判断是否是回文串
        left = 0
        right = len(string) - 1
        while left < right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        return True

    def dfs(self, string, tmp):

        # 字符串已经切割完，记录最终状态
        if not string:
            self.result.append(tmp.copy())
            return

        for i in range(len(string)):
            substr = string[:i + 1]
            # print(substr)
            # 判断当前子集是否是回文
            # if self.is_palindrome(substr):
            # 如果是回文串 记录下
            tmp.append(substr)
            # 接着递归接下来的字符串
            self.dfs(string[i + 1:], tmp)
            # 回溯
            tmp.pop()


if __name__ == '__main__':
    st = 'aab'
    # st = 'abcd'
    s = Solution()
    print(s.partition(st))

    ''' 横向遍历
    纵                aab
    向              /  |  \ 
    递             /   |   X   剪枝 
    归           a     aa  aab
    遍          / X   /
    历         a  ab b
              / 
             b    
    '''
