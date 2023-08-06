def main(data):
    a = [1, 2, 4]
    offsets = []
    for i in range(50):
        if i < 3:
            offsets.append(a[i])
        else:
            offsets.append(offsets[i - 1] + offsets[i - 2] + offsets[i - 3])

    result = []
    for j in range(len(data)):
        # 取模为了防止溢出
        tmp = chr((ord(data[j]) - 97 + offsets[j]) % 26 + 97)
        result.append(tmp)
    print(''.join(result))


s = 'abcde'
s = 'xy'
s = list(s)
main(s)
