"""
输入：[1,8,6,2,5,4,8,3,7]
输出：49
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

输入：height = [1,1]
输出：1

思路
1、因为装水 所以要取 left 和 right 高度较低的 为高h
2、宽度为 left 和 right的距离w 计算面积
3、因为要取最大的面积，比较left 和 right 较小的一个并移动
"""


class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        area = 0
        while left < right:
            h = min(height[left], height[right])
            w = right - left

            area = max(area, h * w)
            # 如果left指的高度较小，那就移动left
            # 如果right指的高度小，那就移动right
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        print(area)


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    height = [1, 1]
    s = Solution()
    s.maxArea(height)
