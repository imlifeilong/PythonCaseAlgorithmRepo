def main(data, n, x):
    count = 0
    for i in range(n):
        for j in range(i, n):
            # print(data[i:j + 1])
            # i -> j+1 所有子区间
            if sum(data[i:j + 1]) >= x:
                count += 1
    print(count)


n = 3
x = 7
s = '3 4 7'.split()

n = 10
x = 10000000
s = '1 2 3 4 5 6 7 8 9 10'.split()

data = list(map(int, s))

main(data, n, x)
