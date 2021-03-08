from typing import List

'''
二进制手表顶部有 4 个 LED 代表 小时（0-11），底部的 6 个 LED 代表 分钟（0-59）。

每个 LED 代表一个 0 或 1，最低位在右侧。



例如，上面的二进制手表读取 “3:25”。

给定一个非负整数 n 代表当前 LED 亮着的数量，返回所有可能的时间。

 

示例：

输入: n = 1
返回: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
 

提示：

输出的顺序没有要求。
小时不会以零开头，比如 “01:00” 是不允许的，应为 “1:00”。
分钟必须由两位数组成，可能会以零开头，比如 “10:2” 是无效的，应为 “10:02”。
超过表示范围（小时 0-11，分钟 0-59）的数据将会被舍弃，也就是说不会出现 "13:00", "0:61" 等时间。

'''


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
