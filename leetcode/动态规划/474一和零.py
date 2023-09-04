'''
输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
输出：4
解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。


'''

from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        res = self.process(0, strs, m, n)
        print(res)

    def process(self, index, strs, m, n):
        # 当所有的值取完时，退出
        if index == len(strs):
            return 0
        one_count = list(strs[index]).count('1')
        zero_count = list(strs[index]).count('0')
        # 当前值中 0的数量或1的数量比 目标值的多时，去下个位置
        if m - zero_count < 0 or n - one_count < 0:
            return self.process(index + 1, strs, m, n)
        # 取当前位置，取完后，去下个位置，数量加1
        p1 = self.process(index + 1, strs, m - zero_count, n - one_count) + 1
        # 不取当前位置，去下个位置
        p2 = self.process(index + 1, strs, m, n)
        return max(p1, p2)


if __name__ == '__main__':
    s = Solution()
    strs = ["10", "0001", "111001", "1", "0"]
    m = 5
    n = 3
    strs = ["10", "0", "1"]
    m = 1
    n = 1
    s.findMaxForm(strs, m, n)
