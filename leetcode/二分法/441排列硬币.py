class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 1
        right = n
        while left < right:
            mid = (left + right) // 2

            if mid * (mid + 1) // 2 <= n:
                # 如果计算的值小了，说明中间值小，则需要再右边继续找，所以left就从mid+1开始
                left = mid
            else:
                # 如果大了，说明中间的值大，则需要再左边继续找，因为左闭右开所以right可以是mid
                right = mid - 1

        # 如果没找到，则返回-1
        # 再此题中，需要找到小于等于目标值，所以如果等于直接返回mid，如果到最后都没相等的值，则返回此时的mid
        return left


if __name__ == '__main__':
    n = 8
    s = Solution()
    res = s.arrangeCoins(n)
    print(res)
