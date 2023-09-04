class Solution:
    def numDecodings(self, s):

        res = self.process(0)
        self.s = s
        self.cache = {}
        res = self.process_cache(0)
        return res

    def process(self, index):
        # 当扫完整个序列的时候，返回一种方法
        if index >= len(s):
            return 1

        # 每一个单独是0的时候，只能和前一位进行组合 比如 10 20
        # 所以遇到这种情况的时候，不能单独组合
        if s[index] == '0':
            return 0

        # 分两种情况
        # 选一个字符的情况
        p1 = self.process(index + 1)
        p2 = 0
        # 选两个字符的情况， 必须是两位，但是再选的时候需要判断下，是否超过26
        p2str = s[index:index + 2]
        if len(p2str) == 2 and int(p2str) <= 26:
            p2 = self.process(index + 2)
        # 两中情况的方法合计
        return p1 + p2

    def process_cache(self, index):
        # 记忆化
        if index in self.cache:
            return self.cache[index]
        if index >= len(self.s):
            self.cache[index] = 1
        elif self.s[index] == '0':
            self.cache[index] = 0
        else:
            p1 = self.process_cache(index + 1)
            p2 = 0
            # 选两个字符的情况， 必须是两位，但是再选的时候需要判断下，是否超过26
            p2str = self.s[index:index + 2]
            if len(p2str) == 2 and int(p2str) <= 26:
                p2 = self.process_cache(index + 2)
            self.cache[index] = p1 + p2

        return self.cache[index]


if __name__ == '__main__':
    s = "20216"
    # s = "06"
    # s = "12"
    obj = Solution()
    res = obj.numDecodings(s)
    print(res)
