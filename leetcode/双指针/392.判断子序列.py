class Solution:
    def isSubsequence_brute(self, s: str, t: str) -> bool:
        # 记录在t中当前查找的起始位置
        start = 0

        # 遍历s中的每个字符
        for char in s:
            found = False

            # 在t中从start位置开始查找当前字符
            for i in range(start, len(t)):
                if t[i] == char:
                    found = True
                    start = i + 1  # 更新下次查找的起始位置
                    break  # 找到后就跳出内层循环

            # 如果在t中没找到当前字符，返回False
            if not found:
                return False

        # s中所有字符都找到了
        return True

    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0  # s的指针
        j = 0  # t的指针

        # 同时遍历两个字符串
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                # 找到匹配，s的指针向后移动
                i += 1
            # 无论是否匹配，t的指针都要向后移动
            j += 1

        # 如果s的所有字符都匹配到了，i会等于s的长度
        return i == len(s)


def main():
    solution = Solution()

    # 测试示例1
    s1 = "abc"
    t1 = "ahbgdc"
    print("Example 1:")
    print(f"s = \"{s1}\", t = \"{t1}\"")
    print(f"Result: {solution.isSubsequence_brute(s1, t1)}")
    print(f"Result: {solution.isSubsequence(s1, t1)}")
    print("Expected: True\n")

    # 测试示例2
    s2 = "axc"
    t2 = "ahbgdc"
    print("Example 2:")
    print(f"s = \"{s2}\", t = \"{t2}\"")
    print(f"Result: {solution.isSubsequence_brute(s2, t2)}")
    print(f"Result: {solution.isSubsequence(s2, t2)}")
    print("Expected: False")


if __name__ == "__main__":
    main()
