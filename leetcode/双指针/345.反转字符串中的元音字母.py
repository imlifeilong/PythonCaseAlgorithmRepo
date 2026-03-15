class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        反转字符串中的所有元音字母，保持非元音字母的位置不变
        :param s: 输入的原始字符串（不可变类型）
        :return: 反转元音字母后的字符串
        """
        # 定义元音字母集合（包含大小写），使用set实现O(1)时间复杂度的快速查找
        vowels = set('aeiouAEIOU')

        # Python中字符串是不可变对象，无法直接修改字符，因此转换为列表便于原地修改
        chars = list(s)
        # 初始化双指针：左指针指向字符串头部，右指针指向字符串尾部
        left, right = 0, len(chars) - 1

        # 外层循环：只要左指针在右指针左侧，就继续寻找并交换元音字母（避免重复交换或越界）
        while left < right:
            # 内层循环：移动左指针，直到找到元音字母 或 左指针追上右指针
            # 条件：left < right 防止指针越界；chars[left] not in vowels 表示当前字符不是元音
            while left < right and chars[left] not in vowels:
                left += 1  # 左指针右移，寻找下一个字符

            # 内层循环：移动右指针，直到找到元音字母 或 右指针被左指针追上
            while left < right and chars[right] not in vowels:
                right -= 1  # 右指针左移，寻找前一个字符

            # 此时左右指针均找到有效元音字母，且左指针在右指针左侧，执行交换操作
            if left < right:
                # 交换两个元音字母的位置（Python特有解构赋值，无需临时变量）
                chars[left], chars[right] = chars[right], chars[left]
                left += 1  # 左指针右移，准备寻找下一个元音
                right -= 1  # 右指针左移，准备寻找下一个元音

        # 将修改后的字符列表转换回字符串，返回最终结果
        return ''.join(chars)


# 程序入口：当该脚本直接运行时，执行以下测试代码
if __name__ == "__main__":
    # 创建Solution类的实例，用于调用反转元音字母的方法
    solution = Solution()

    # 测试示例1：普通简单字符串（包含2个元音：e和o）
    test1 = "hello"
    print(f"Input: {test1}")
    print(f"Output: {solution.reverseVowels(test1)}")

    # 测试示例2：包含多个元音的字符串（元音：e、e、o）
    test2 = "leetcode"
    print(f"\nInput: {test2}")
    print(f"Output: {solution.reverseVowels(test2)}")

    # 测试示例3：仅包含大小写元音的字符串（边界情况：2个元音，大小写不同）
    test3 = "aA"
    print(f"\nInput: {test3}")
    print(f"Output: {solution.reverseVowels(test3)}")

    # 测试示例4：混合大小写和复杂结构的字符串（元音：I、e、e、A）
    test4 = "IceCreAm"
    print(f"\nInput: {test4}")
    print(f"Output: {solution.reverseVowels(test4)}")