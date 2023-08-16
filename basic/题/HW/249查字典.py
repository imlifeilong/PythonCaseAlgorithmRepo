def main(s, k):
    ok = True
    for c in s:
        if c.startswith(k):
            print(c)
            ok = False
    if ok:
        print(-1)


s = 'a b c'.split()
k = 'b'

s = 'a ab abc abcd'.split()
k = 'abc'

s = 'b c d'.split()
k = 'a'
main(s, k)
