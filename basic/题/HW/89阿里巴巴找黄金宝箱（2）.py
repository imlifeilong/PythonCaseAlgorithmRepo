def main(s):
    # 统计集合个数
    count = {}
    for c in s:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1

    length = len(count)

    data = sorted(count.values())
    # 根据集合个数排序，从大的开始累计，超过总数的一半就停止
    for i in range(length):
        # 从后往前
        cur = data[length - i - 1:]
        cur = data[-(i + 1):]
        if sum(cur) >= len(s) // 2:
            print(i + 1)
            break


# s = '6,6,6,6,3,3,3,1,1,5'.split(',')
# s = '1,1,1,1,3,3,3,6,6,8'.split(',')
s = '2,2,2,2'.split(',')

main(s)
