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
        # 当用完最后一块硬币时，还没兑换完，需要舍弃，返回无穷大（因为要取最小值）
        if index == len(coins):
            return float('inf')
        # 当前硬币比目标值大，换下个硬币
        if coins[index] > amount:
            return self.process(index + 1, coins, amount)
        # 使用当前硬币，还可以选择当前硬币，目标值减去当前硬币
        p2 = self.process(index, coins, amount - coins[index]) + 1
        # 不适用当前硬币，去换下个硬币
        p1 = self.process(index + 1, coins, amount)
        return min(p1, p2)


if __name__ == '__main__':
    s = Solution()
    coins = [1, 2, 5]
    amount = 11
    # coins = [2]
    # amount = 3
    # coins = [1]
    # amount = 0
    s.coinChange(coins, amount)
