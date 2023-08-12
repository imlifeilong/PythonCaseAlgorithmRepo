def main(s):
    # 只能是数字或小写字母
    for c in s:
        if not (c.isdigit() or c.islower()):
            print('!error')
            return
    result = []
    i = 0
    while i < len(s):
        # 如果当前字符是数字，大于2是计算后面跟着的字符长度
        # 指针指向下一位
        if s[i].isdigit():
            if int(s[i]) > 2:
                result.append(int(s[i]) * s[i + 1])
                i += 1
            else:
                print('!error')
                return
        else:
            result.append(s[i])
        i += 1
    print(result)


s = '4d@A'
s = '4dff'
s = '3abb4cd'
main(s)
