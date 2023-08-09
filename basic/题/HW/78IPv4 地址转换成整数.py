def main(ip):
    length = len(ip)
    if length != 4:
        print('invalid IP')
        return
    total = 0
    for i in range(length):
        if i == 0 and (1 > ip[i] or ip[i] > 128):
            print('invalid IP')
            return
        if 0 > ip[i] or ip[i] > 255:
            print('invalid IP')
            return
        total += ip[i] << (8 * (3 - i))
    print(total)


ip = '120#101#1#285'.split('#')
ip = '128#0#255#255'.split('#')
ip = list(map(int, ip))
main(ip)


