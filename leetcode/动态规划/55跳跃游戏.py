from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        self.length = len(nums)
        return self.process(0, nums, self.length)

    def process(self, index, nums, length):
        """
        在index位置能否跳到最后一位
        :param index:
        :return:
        """

        if index < self.length and nums[index] >= length:
            return True
        if index >= self.length:
            return False

        p = False

        # [1, nums[index]] 表示 从跳一步 到跳当前值的步数
        for i in range(1, nums[index] + 1):
            # 如果跳1步 下次位置就是 index +1 跳2步就是index+2 跳i步 就是index+i 剩下的长度就是 length - i
            # | 使用或 是因为只要有一种可能行
            p |= self.process(index + i, nums, length - i)
        return p

    def process_dp(self):
        pass


if __name__ == '__main__':
    s = Solution()
    nums = [2, 3, 1, 1, 4]
    # nums = [3, 2, 1, 0, 4]
    # nums = [0]
    res = s.canJump(nums)
    print(res)
