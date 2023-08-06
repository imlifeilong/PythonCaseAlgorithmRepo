def max_string_count(s):
    res = []
    length = len(s)
    i = 0
    while i < length:
        count = 1
        c = s[i]

        # 找当前值的连续个数
        j = i + 1  # 从下一位开始
        while j < len(s):
            if s[j] == c:
                count += 1
                j += 1  # 第二次指针移动
                i += 1  # 第一层指针移动
            else:
                break
        i += 1
        res.append(f'{count}{c}')
    return ''.join(res)


def main(n):
    x = '1'
    if n == 0:
        print(x)
        return

    for i in range(1, n + 1):
        x = max_string_count(x)
        print(i, x)

    print("result --- ", x)


main(8)
