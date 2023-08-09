def main(m, n, R):
    result = []
    for i in range(len(m)):
        for j in range(len(n)):
            # 每次找到n中一个数与m中的值进行比较，找到后再进行下一个m值
            if m[i] <= n[j] and n[j] - m[i] <= R:
                result.append((m[i], n[j]))
                break

    for row in result:
        print(*row)


R = 5
m = list(map(int, '1 5 5 10'.split()))
n = list(map(int, '1 3 8 8 20'.split()))
main(m, n, R)
