def main(s):
    mapping = {}
    for c in s:
        if c not in mapping:
            mapping[c] = 1
        else:
            mapping[c] += 1
    # 首先按照字母的小写形式进行排序，然后按照原始字母进行排序。这样就实现了小写字母在前，大写字母在后的排序
    res = sorted(mapping.items(), key=lambda x: (-x[1], (ord(x[0]) < 95)))

    ress = [f'{x}:{y}' for x, y in res]
    print(';'.join(ress))


# s = 'xyxyXX'
s = 'abababb'
s = 'aabbCCssDDD'
main(s)
