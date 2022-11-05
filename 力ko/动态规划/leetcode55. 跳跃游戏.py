from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        return self.process(0, nums)

    def process(self, index, nums):
        """
        在index位置能否跳到最后一位
        :param index:
        :return:
        """
        nlen = len(nums)
        if index == nlen - 2:
            if nums[index] >= 1:
                return True
            else:
                return False
        return self.process(index + 1, nums)

    def process_dp(self):
        pass


if __name__ == '__main__':
    s = Solution()
    nums = [2, 3, 1, 1, 4]
    nums = [3, 2, 1, 0, 4]
    nums = [0]
    res = s.canJump(nums)
    print(res)
