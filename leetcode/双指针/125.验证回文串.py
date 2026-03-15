class Solution:
    def isPalindrome_brute(self, s: str) -> bool:
        # 过滤字符串，只保留字母和数字，并转换为小写
        filtered_str = ''.join(ch.lower() for ch in s if ch.isalnum())

        # 创建反转字符串
        reversed_str = filtered_str[::-1]

        # 比较原过滤字符串和反转后的字符串
        return filtered_str == reversed_str

    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # 移动左指针，直到找到字母或数字
            while left < right and not s[left].isalnum():
                left += 1

            # 移动右指针，直到找到字母或数字
            while left < right and not s[right].isalnum():
                right -= 1

            # 比较字符（忽略大小写）
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


if __name__ == "__main__":
    solution = Solution()

    # 测试示例
    test1 = "A man, a plan, a canal: Panama"
    print(f"Test 1: {solution.isPalindrome_brute(test1)}")
    print(f"Test 1: {solution.isPalindrome(test1)}")

    test2 = "race a car"
    print(f"Test 2: {solution.isPalindrome_brute(test2)}")
    print(f"Test 2: {solution.isPalindrome(test2)}")

    test3 = " "
    print(f"Test 3: {solution.isPalindrome_brute(test3)}")
    print(f"Test 3: {solution.isPalindrome(test3)}")
