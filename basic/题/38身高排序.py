def main(data, h):
    res = sorted(data, key=lambda x: (abs(x - h), x))
    print(res)
    print(' '.join(map(str, res)))


s = '''95 96 97 98 99 101 102 103 104 105'''.split()
data = list(map(int, s))
h = 100
main(data, h)
