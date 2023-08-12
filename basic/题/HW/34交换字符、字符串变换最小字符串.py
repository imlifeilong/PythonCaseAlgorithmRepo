def main(s):
    data = list(s)
    minval = data[0]
    index = 0

    for i in range(1, len(data)):
        if data[i] < minval:
            # 找到较小的值，和对应的索引位置
            minval = data[i]
            index = i
    # 找到最小的位置，与第一位替换
    if index != 0:
        data[index] = data[0]
        data[0] = minval
    print(''.join(data))


s = 'bcdefa'
s = 'abcdef'
main(s)
