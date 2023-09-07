class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        self.num = num
        self.length = len(self.num)
        self.flag = False
        self.backtrack(0, [])
        print(self.flag)

    def backtrack(self, start, tmp):
        if start == self.length and ''.join(map(str, tmp)) == self.num:
            self.flag = True
            return

        for i in range(start, self.length):
            tmpnum = self.num[start:i + 1]
            print(tmp, tmpnum)
            if len(tmp) > 1 and tmp[-2] + tmp[-1] != int(tmpnum):
                print('====')
                continue

            tmp.append(int(tmpnum))
            print(tmpnum)
            # if len(tmp) > 1 and tmp[i - 2] + tmp[i - 1] == int(tmpnum):
            self.backtrack(i + 1, tmp)
            tmp.pop()


if __name__ == '__main__':
    num = "1123583"
    # num = "199100199"
    s = Solution()
    s.isAdditiveNumber(num)
