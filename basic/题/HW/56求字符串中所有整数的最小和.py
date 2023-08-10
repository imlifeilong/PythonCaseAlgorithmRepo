def main(s):
    res = 0
    index = 0
    while index < len(s):
        # 处理负数
        if s[index] == '-':
            # 找到负号后面的所有数字
            tmp = []
            for j in range(index + 1, len(s)):
                if s[j].isdigit():
                    tmp.append(s[j])
                else:
                    break
            # 负号后面有数字
            if tmp:
                # 索引位置更新到负数之后的位置
                index += len(tmp) + 1
                res -= int(''.join(tmp))
                continue
        if s[index].isdigit():
            res += int(s[index])
        index += 1

    print(res)


s = '99-13bb-12-3-4a-a'
# s = 'bb1234-aa'
main(s)
