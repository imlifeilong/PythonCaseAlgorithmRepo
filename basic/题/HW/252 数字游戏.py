def main(data, n, m):
    '''前缀和'''
    pre_sum = 0
    is_true = False
    remainders = set()
    for i in range(n):
        pre_sum = (pre_sum + data[i]) % m
        if pre_sum in remainders:
            is_true = True
            break
        remainders.add(pre_sum)

    print(1 if is_true else 0)


n, m = 6, 7

s = '2 12 6 3 5 5'.split()
n, m = 10, 11
s = '1 1 1 1 1 1 1 1 1 1'.split()

data = list(map(int, s))
main(data, n, m)
