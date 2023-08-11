def main(s):
    indexs = []
    indexs.append(-1)  # 添加左边界
    # 找到所有字母的索引
    for i, c in enumerate(s):
        if 'a' <= c <= 'z' or 'A' <= c <= 'Z':
            indexs.append(i)
    indexs.append(len(s))  # 添加右边界，处理只有1个字母，或者indexs中间隔小于2的情况 a123b
    # 然后根据字母索引之间的间隔，得知连续数字的长度
    maxval = -1
    for j in range(len(indexs) - 2):
        tmp = indexs[j + 2] - indexs[j]

        if tmp > 2:  # 间隔大于2的情况中间可以插一个数字，
            maxval = max(tmp - 1, maxval)  # 更新最大值
    print(maxval)


s = 'abC124ACb'
s = 'a123b'
# s = 'a'
# s = 'aa5'
main(s)
