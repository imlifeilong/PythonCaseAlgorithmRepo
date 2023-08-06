def main(data, t):
    length = len(data)
    mins = []
    for i in range(length):
        for j in range(i + 1, length):
            for h in range(j + 1, length):
                tmp = data[i] + data[j] + data[h]
                if tmp <= t:
                    mins.append(tmp)

    if mins:
        mins.sort()
        print(mins[-1])
    else:
        print(-1)


s = "23,26,36,27".split(',')
data = list(map(int, s))
t = 78

# s = "23,30,40".split(',')
# data = list(map(int, s))
# t = 26

main(data, t)
