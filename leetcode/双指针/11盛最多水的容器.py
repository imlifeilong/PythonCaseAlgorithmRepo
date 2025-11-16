# https://leetcode.cn/problems/container-with-most-water/
class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0  # 最大面积初始值
        while left < right:
            # 容器的面积由 短板高度 和 两柱间距 共同决定
            # 短板高度
            current_height = min(height[left], height[right])
            # 两柱间距
            current_width = right - left
            # 面积
            current_area = current_width * current_height

            max_area = max(max_area, current_area)
            # 移动短板指针
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        print(max_area)
        return max_area


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    height = [1, 1]
    s = Solution()
    s.maxArea(height)
