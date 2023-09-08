class Solution:
    def letterCasePermutation(self, s):
        self.s = s
        self.length = len(self.s)
        self.result = []
        self.backtrack(0, 0, [])
        return self.result

    def backtrack(self, h, start, tmp):
        # h 表示要递归的深度 深度达到 字符串长度时 终止递归
        # start 每层遍历开始位置
        # tmp 栈 存符合条件的值

        if h == self.length:
            self.result.append(''.join(tmp))
            return
        # 因为各层遍历的时候 值是不能重复的，所以需要从指定的位置开始遍历
        for i in range(start, self.length):
            tmpstr = self.s[i]
            if tmpstr.isalpha():
                # 当前的字符如果是字母 就有两种情况 大写获取小写，
                for j in range(2):
                    if j == 0:
                        # 可以使用 tmpstr.swapcase() 代替下面逻辑

                        # 第一种情况 如果是小写字母
                        if tmpstr.islower():
                            # 就变为大写字母
                            tmp.append(tmpstr.upper())
                        else:
                            # 如果是小写字母 就变为大写字母
                            tmp.append(tmpstr.lower())
                    else:
                        # 第二中情况就是将原字母 入栈
                        tmp.append(tmpstr)

                    # 然后分别去下一层，高度加1 并且下一层的位置是从当前元素的下一位开始的
                    self.backtrack(h + 1, i + 1, tmp)
                    tmp.pop()
            else:
                # 如果是不是字母就直接去下一层
                tmp.append(tmpstr)
                self.backtrack(h + 1, i + 1, tmp)
                tmp.pop()


if __name__ == '__main__':
    s = 'a1b2'
    # s = "3z4"
    # s = "C"
    obj = Solution()
    res = obj.letterCasePermutation(s)
    print(res)
