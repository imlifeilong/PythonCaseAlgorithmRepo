"""
 输入："aabcccccaaa"
 输出："a2b1c5a3"


输入："abbccd"
 输出："abbccd"
 解释："abbccd"压缩后为"a1b2c2d1"，比原字符串长度更长。
"""


def compress(s):
    left, right = 0, 0
    res = []
    while left < len(s):

        # 右指针不越界，并且左右指针指向的值相等时，右指针向前一位，直到不相等或者末尾
        while right < len(s) and s[left] == s[right]:
            right += 1

        # 计算相同字符串的长度，拼接
        res.append(s[left] + str(right - left))
        # 左指针指向右指针的位置，重新开始判断
        left = right
    # print(res)
    string = ''.join(res)
    # print(string)
    return string if len(string) < len(s) else s


s = "aabcccccaaa"
# s = "abbccd"
res = compress(s)
print(res)
