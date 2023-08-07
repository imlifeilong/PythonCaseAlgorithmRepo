def main(s):
    text = s.split(',')
    if len(text) == 0 or s == ',':
        print('/')
        return

    url = '/' + text[0].strip('/') + '/' + text[1].strip('/')
    print(url)


s = '/abc/,/bcd'
s = '/acm,/bb'
s = '/acd,bef'
s = ','
main(s)
