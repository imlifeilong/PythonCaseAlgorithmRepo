class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        self.num = num
        self.length = len(self.num)
        self.flag = False
        self.backtrack(0, [])
        return self.flag

    def backtrack(self, start, tmp):
        # len(tmp) >= 3 是剪枝
        # start == length 表示深度已经遍历完成了，如果满足条件的化 就标志为True
        if start == self.length and len(tmp) >= 3:
            self.flag = True
            return

        # 每次所选的数不能又重复，所以都要从指定的位置开始
        for i in range(start, self.length):
            # 截取一个数字
            tmpnum = self.num[start:i + 1]
            # 如果截取的数字是0开始的则不符合，0只能再末尾或中间位置 如 0 10 101 不能是 01 011
            # break 是因为 后面的可能都不符合所以直接跳出循环
            if len(tmpnum) > 1 and tmpnum[0] == '0':
                break

            # 通过判断 tmp 中最后两个数加起来灯与当前截取的数字时
            # 可以优化的点 如果 tmpnum 大于 tmp[-2]+tmp[-1]时 后面的数也会大于，直接break
            # if len(tmp) > 1 and tmp[-2] + tmp[-1] > int(tmpnum):break
            if len(tmp) > 1 and tmp[-2] + tmp[-1] != int(tmpnum):
                continue

            # 如果符合条件，记录当前值，去下一层进行递归，下一层要从当前元素的下一个位置开始所以时i+1
            tmp.append(int(tmpnum))
            self.backtrack(i + 1, tmp)
            tmp.pop()


if __name__ == '__main__':
    num = "112358"
    num = "199100199"
    # num = "1023"
    num = "101"
    s = Solution()
    res = s.isAdditiveNumber(num)
    print(res)
