def main(data):
    count = 0
    for row in data:
        length = len(row)

        # 3个连续的位置可以停1辆
        while length > 3:
            count += 1
            length -= 3

        if length == 0:
            continue
        # 2个或者1个分别可以停1辆
        count += 1
    print(count)


s = '1,1,0,0,1,1,1,0,1'.replace(',', '')
data = s.split('0')
main(data)
