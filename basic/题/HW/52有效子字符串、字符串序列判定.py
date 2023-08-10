def main(s1, s2):
    if len(s2) < len(s1):
        print(-1)
        return
    # 两个指针分别指向s1 和 s2
    index1 = index2 = 0

    while index1 < len(s1) and index2 < len(s2):
        if s1[index1] == s2[index2]:
            # 字符相等的时候，s1指向下一位去
            index1 += 1
        else:
            # 不相等的时候 s2指向下一位去
            index2 += 1
    # 如果s1走到最末尾则表示s2中包含了s1所有的字符
    if index1 == len(s1):
        print(index1)
    else:
        print(-1)


s1 = 'acce'
s2 = 'abcde'
s1 = 'fgh'
s2 = 'abcde'
main(s1, s2)
