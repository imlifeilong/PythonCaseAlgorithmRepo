from typing import List


class Solution:
    mapping = [480, 240, 120, 60, 32, 16, 8, 4, 2, 1]
    result = []

    def readBinaryWatch(self, num: int) -> List[str]:
        self.dfs(0, num, self.mapping, [])
        return self.result

    def dfs(self, index, num, mapping, tmp):
        if index == num:
            _time = self.m2h(tmp)
            print(_time)
            if _time:
                self.result.append(_time)
            return

        for i in range(len(mapping)):
            tmp.append(mapping[i])
            self.dfs(index + 1, num, mapping[i + 1:], tmp)
            tmp.pop()

    def m2h(self, m):
        ms = sum(m)
        print(ms)
        hour = ms // 60

        if hour >= 12: return
        min = ms % 60

        min = '0%s' % min if min < 10 else '%s' % min
        hour = '%s' % hour
        return '%s:%s' % (hour, min)


if __name__ == '__main__':
    s = Solution()
    res = s.readBinaryWatch(1)
    print(len(res))
    print(res)
    # s.m2h([480, 32])
