'''

输入：amount = 5, coins = [1, 2, 5]
输出：4
解释：有四种方式可以凑成总金额：
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
'''

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        res = self.process(0, amount, coins)
        print(res)

    def process(self, index, amount, coins):
        # 目标值为0 时，这种换法可行，返回1
        if amount == 0:
            return 1
        # 换掉所有硬币时，目标值还不为0，换法不可行
        if index == len(coins):
            return 0
        # 总金额小于当前的硬币时，必须到下一个兑换
        if amount - coins[index] < 0:
            return self.process(index + 1, amount, coins)
        # 使用当前硬币兑换，还可以使用当前硬币，目标值减去当前硬币
        p1 = self.process(index, amount - coins[index], coins)
        # 不使用当前硬币，去换下个硬币
        p2 = self.process(index + 1, amount, coins)
        return p1 + p2


if __name__ == '__main__':
    s = Solution()
    amount = 5
    coins = [1, 2, 5]
    # amount = 3
    # coins = [2]
    # amount = 10
    # coins = [10]
    s.change(amount, coins)
