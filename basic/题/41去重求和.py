def main(data, n):
    tmp = list(set(data))
    tmp.sort()
    print(tmp)
    if len(tmp) < 4:
        print('-1')
        return
    print(sum(tmp[:n]) + sum(tmp[-n:]))


s = '95 88 83 64 100'.split()
n = 2

# s = '3 2 3 4 2'.split()
# n = 2
data = list(map(int, s))

main(data, n)
