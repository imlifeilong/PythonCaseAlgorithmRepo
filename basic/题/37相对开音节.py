def main(s):
    count = 0
    meta = ('a', 'e', 'i', 'o', 'u')
    for text in s.split():
        # 字符串长度不能小于4，必须全是小写字母，不能包含其他字符
        if len(text) >= 4 and text.isalpha() and text.islower():
            # 过滤不是字母的字符
            tmp = list(text)
            left, right = 0, len(tmp) - 1
            while left < right:
                tmp[left], tmp[right] = tmp[right], tmp[left]
                left += 1
                right -= 1

            # len(tmp)-3 从后往前算，保持不越界
            for i in range(len(tmp) - 3):
                content = tmp[i:i + 4]
                if content[0] not in meta and content[1] in meta and content[2] not in meta and content[2] != 'r' and \
                        content[3] == 'e':
                    count += 1
    print(count)


s = 'ekam a ekac'
# s = '!ekam a ekekac'
main(s)
