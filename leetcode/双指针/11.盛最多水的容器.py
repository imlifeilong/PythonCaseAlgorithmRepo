# https://leetcode.cn/problems/container-with-most-water/
class Solution:

    def maxArea_brute(self, height):
        """
        使用暴力枚举法计算盛最多水的容器
        :param height: 整数列表，代表每个位置的高度
        :return: 最大容量
        """
        n = len(height)
        max_area = 0

        # 遍历所有可能的左端点
        for i in range(n):
            # 遍历所有可能的右端点（右端点必须在左端点右侧）
            for j in range(i + 1, n):
                # 计算当前容器的宽度和高度
                width = j - i
                current_height = min(height[i], height[j])
                # 计算当前容量
                area = width * current_height
                # 更新最大容量
                if area > max_area:
                    max_area = area
        print(max_area)
        return max_area

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
    # height = [1, 1]
    s = Solution()
    s.maxArea(height)
    s.maxArea_brute(height)
