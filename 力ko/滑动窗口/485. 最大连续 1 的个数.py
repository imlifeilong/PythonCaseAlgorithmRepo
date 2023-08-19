"""
题目：给定一个二进制数组， 计算其中最大连续 1 的个数。
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        # 使用滑动窗口解法
        n = len(nums)
        left = 0
        right = 0
        count = 0
        while right < n:
            # 判断right指向位置的值是否时1 如果是1 就继续移动right
            if nums[right] == 1:
                right += 1
            # 如果right指向的不是1，就必须移动left，以保证left和right之间是连续的1
            else:
                # 如果right指向的值是0，则将right移动到值是1的位置，此时left也跟上right的位置，重新开始滑动right
                right += 1
                left = right
            # 记录当前left和right的长度，即连续1的个数，和之前的记录种比较，取较大的一个
            count = max(count, right - left)
        print(count)
        return count


if __name__ == '__main__':
    nums = [1, 1, 0, 1, 1, 1]
    # nums = [1, 0, 1, 1, 0, 1]
    s = Solution()
    s.findMaxConsecutiveOnes(nums)
