def main(data):
    # 记录每个字符出现的次数
    mapping = {}
    for c in data:
        if c in mapping:
            mapping[c] += 1
        else:
            mapping[c] = 1

    # 根据次数和原来的值进行排序
    res = sorted(mapping.items(), key=lambda x: (-x[1], x[0]))

    print(','.join([x[0] for x in res]))


s = '1,3,3,3,2,4,4,4,5'.split(',')
s = '2,1,1,1,3,3,3,2,4,4,4,5,5,5'.split(',')
main(s)
