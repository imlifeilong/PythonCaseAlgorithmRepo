def main(data):
    data = list(set(data))
    data.sort()
    length = len(data)
    text = '0'
    for x in range(length - 1, -1, -1):
        # 一个数可以出现两次， y和z的范围都是x
        for y in range(x):
            for z in range(x):
                if data[x] == data[y] + 2 * data[z]:
                    text = f'{data[x]} {data[y]} {data[z]}'
                    # print(data[x], data[y], data[z])
    print(text)


s = '2 7 3 0'.split()
# s = '1 1 1'.split()
data = list(map(int, s))
main(data)
