"""
[start:i+1]

a     b     c     d
            回溯第3层 2 - 4
a     b     cd
      回溯第2层 1-3
a     bc     d
      回溯第2层 1-4
0     1
a     bcd

回溯第1层 0-2
ab     c     d

       回溯第2层 2-4
ab     cd

回溯第1层 0-3
abc     d

回溯第1层0-4
abcd

"""


class Solution:
    def partition(self, s):
        self.result = []
        self.s = s
        self.length = len(self.s)
        self.backtrack(0, [])

    def backtrack(self, start, tmp):
        # start 要截取的字符串的开始位置
        # tmp 临时栈 用于存放元素

        # start == length表示扫描到字符串末尾了，后面没有字符了，就终止递归
        if start == self.length:
            print('     '.join(tmp))

            return

        for i in range(start, self.length):
            tmpstr = self.s[start:i + 1]
            # print(start, i+1, tmpstr)
            # 去下一层遍历的时候，从当前位置的下一位开始，并且递归的深度加1
            tmp.append(tmpstr)
            self.backtrack(i + 1, tmp)
            tmp.pop()


if __name__ == '__main__':
    st = 'abcd'
    # st = 'abv'
    s = Solution()
    s.partition(st)
