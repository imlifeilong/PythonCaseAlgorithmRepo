"""
输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1

"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = self.process(0, coins, amount)
        res = res if res != float("inf") else -1
        print('==========', res)

    def process(self, index, coins, amount):
        # 不需要取硬币了
        if amount == 0:
            return 0
        # 返回超级大的数据，说明已经取不到硬币了
        if index == len(coins):
            return float('inf')
        if coins[index] > amount:
            return self.process(index + 1, coins, amount)
        p2 = self.process(index, coins, amount - coins[index]) + 1
        p1 = self.process(index + 1, coins, amount)
        return min(p1, p2)


if __name__ == '__main__':
    s = Solution()
    coins = [1, 2, 5]
    amount = 11
    coins = [2]
    amount = 3
    coins = [1]
    amount = 0
    s.coinChange(coins, amount)
