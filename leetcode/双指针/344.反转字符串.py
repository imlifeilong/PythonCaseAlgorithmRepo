from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1
        # 相向移动指针，交换字符
        while left < right:
            # 交换左右指针指向的字符
            s[left], s[right] = s[right], s[left]
            # 左指针右移，右指针左移
            left += 1
            right -= 1


if __name__ == "__main__":
    solution = Solution()

    # 测试示例
    s1 = ['h', 'e', 'l', 'l', 'o']
    print(f"Before: {''.join(s1)}")
    solution.reverseString(s1)
    print(f"After: {''.join(s1)}")

    s2 = ['H', 'a', 'n', 'n', 'a', 'h']
    print(f"Before: {''.join(s2)}")
    solution.reverseString(s2)
    print(f"After: {''.join(s2)}")
