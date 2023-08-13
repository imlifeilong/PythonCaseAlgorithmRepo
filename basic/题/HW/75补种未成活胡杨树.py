def main(n, m, data, k):
    mapping = []
    for i in range(1, n + 1):
        if i in data:
            mapping.append(0)
        else:
            mapping.append(1)
    print(mapping)




n = 10
m = 3
s = '2 4 7'.split()
k = 1
data = list(map(int, s))
main(n, m, data, k)
