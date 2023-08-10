def main(n):
    print(f'{n}={n}')
    result = []
    for i in range(1, n):
        tmp = []
        for j in range(i, n):
            tmp.append(j)
            # 计算子序列是否等于目标值
            if sum(tmp) == n:
                res = map(str, tmp)
                result.append(f'{n}={"+".join(res)}')
                break

    for row in sorted(result, key=len):
        print(row)
    print('Result:', len(result) + 1)


n = 10
main(n)
