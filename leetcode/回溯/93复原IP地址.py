class Solution:
    def restoreIpAddresses(self, s):
        self.s = s
        self.length = len(self.s)
        self.result = []
        self.backtrack(0, [])
        print(self.result)
        return self.result

    def isipaddr(self, string):
        # 如果是 01 012 这种的也是不符合的
        if len(string) > 1 and string.startswith('0'):
            return False
        # 如果数字超过了255 或者小于0也不符合
        if 0 <= int(string) <= 255:
            return True

        return False

    def backtrack(self, start, tmp):
        # ip地址要分为4段，所以当tmp的长度为4时
        # start == length  并且已经扫完了整个字符串，就可以终止递归
        if len(tmp) == 4 and start == self.length:
            self.result.append('.'.join(tmp[:]))
            return

        # 开始
        for i in range(start, self.length):
            tmpstr = self.s[start:i + 1]

            if self.isipaddr(tmpstr):
                tmp.append(tmpstr)
                self.backtrack(i + 1, tmp)
                tmp.pop()


if __name__ == '__main__':
    s = "25525511135"
    s = "0000"
    s = "101023"
    obj = Solution()
    obj.restoreIpAddresses(s)
