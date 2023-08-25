def main():
    for i in range(1, 10):
        tmp = []
        for j in range(1, i + 1):
            tmp.append(f'{i}*{j}={i * j}')
        print('\t'.join(tmp))
    print('----' * 18)
    for i in range(1, 10):
        tmp = []
        for j in range(i, 10):
            tmp.append(f'{i}*{j}={i * j}')
        print('\t'.join(tmp))


main()
