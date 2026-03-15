from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # 1. 排序
        g.sort()
        s.sort()

        child = 0  # 指向当前要满足的孩子
        cookie = 0  # 指向当前尝试的饼干

        # 2. 双指针遍历
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                # 当前饼干可以满足当前孩子，移动到下一个孩子
                child += 1
            # 无论是否满足，当前饼干都已被尝试，移动到下一个饼干
            cookie += 1

        return child


if __name__ == "__main__":
    solution = Solution()

    # 示例 1
    g1 = [1, 2, 3]
    s1 = [1, 1]
    print(f"示例 1 输出 (双指针解法): {solution.findContentChildren(g1, s1)}")  # 预期输出: 1

    # 示例 2
    g2 = [1, 2]
    s2 = [1, 2, 3]
    print(f"示例 2 输出 (双指针解法): {solution.findContentChildren(g2, s2)}")  # 预期输出: 2
