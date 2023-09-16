class Solution:
    def trap(self, height):
        self.length = len(height)
        # [1, length-1] 第一个和最后一个不能接到雨
        area = 0
        # 找到每一列左右最高的柱子，
        for i in range(1, self.length - 1):
            max_left = max_right = height[i]
            # 找到左边最高的位置
            for left in range(0, i):
                max_left = max(max_left, height[left])
            # 找到右边最高的位置
            for right in range(i + 1, self.length):
                max_right = max(max_right, height[right])
            # 找到左右高度中，比较低的，然后减掉当前柱子的高度，就是当前柱子上能接的水，宽度是1
            area += min(max_left, max_right) - height[i]

        return area

    def trap_dp(self, height):
        self.length = len(height)
        area = 0
        # 记录左变最高柱子
        left_height = [0] * self.length
        # 记录右边最高柱子
        right_height = [0] * self.length
        # 第一个位置 左边最高的位置就是自己
        left_height[0] = height[0]
        # 最后一个位置 右边的最高的位置就是自己
        right_height[self.length - 1] = height[self.length - 1]

        for i in range(1, self.length):
            # 当前节点左边的最高值，是前一个位置的左边最高的柱子高度，和本柱子的高度，比较大的一个
            left_height[i] = max(left_height[i - 1], height[i])

        # 记录当前节点的右边最高的点，当前节点和右边的节点时记录的最高的节点，比较高的
        for j in range(self.length - 2, -1, -1):
            right_height[j] = max(right_height[j + 1], height[j])

        for x in range(1, self.length - 1):
            # 然后计算每个节点的面积，就时能接的水
            area += min(left_height[x], right_height[x]) - height[x]
        print(area)
        return area

    def trap2(self):
        # 接雨水的变种问题
        graps = [[0, 1], [3, 1], [0, 1], [4, 2], [3, 3], [0, 1], [7, 1], [6, 3], [5, 1], [4, 1], [9, 1],
                 [0, 1], [7, 2]]

        self.length = len(graps)
        area = 0
        # 记录左变最高柱子
        left_height = [0] * self.length
        # 记录右边最高柱子
        right_height = [0] * self.length
        # 第一个位置 左边最高的位置就是自己
        left_height[0] = graps[0][0]
        # 最后一个位置 右边的最高的位置就是自己
        right_height[self.length - 1] = graps[self.length - 1][0]

        for i in range(1, self.length):
            left_height[i] = max(left_height[i - 1], graps[i][0])

        for j in range(self.length - 2, -1, -1):
            right_height[j] = max(right_height[j + 1], graps[j][0])

        for x in range(self.length):
            # 计算面积，当前组的高度*宽度就是面积
            area += (min(right_height[x], left_height[x]) - graps[x][0]) * graps[x][1]
        return area


if __name__ == '__main__':
    s = Solution()
    # height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    height = [4, 2, 0, 3, 2, 5]
    res = s.trap(height)
    print(res)
    s.trap_dp(height)
    s.trap2()
