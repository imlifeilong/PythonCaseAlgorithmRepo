def main(data):
    res = []
    for i in range(len(data)):
        # 找当剩下序列中比当前值大的第一个数的索引位置
        for j in range(i + 1, len(data)):
            if data[j] > data[i]:
                res.append(str(j))
                break
        # 如果剩下的序列没有，就记为0
        else:
            res.append('0')
    print(' '.join(res))


s = '123 124 125 121 119 122 126 123'.split()
data = list(map(int, s))
main(data)
