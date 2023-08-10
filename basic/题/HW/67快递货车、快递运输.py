def main(data, n):
    data.sort()
    val = 0
    for i in range(len(data)):
        val += data[i]
        if val > n:
            print(i)
            break


s = '5,10,2,11'.split(',')
s = '5,10,2,11,1'.split(',')
data = list(map(int, s))
n = 20
main(data, n)
