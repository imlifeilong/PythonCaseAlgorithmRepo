def main(data):
    tmplist = []
    for row in data:
        tmplist.append((row.split('/')))

    c1 = []
    c2 = []
    c1.append(int(tmplist[0][0]))
    # 第一位同学选择第一个班
    last_class = c1

    # 从第二位同学开始
    for i in range(1, len(tmplist)):
        curent = tmplist[i]
        # 当前和上一个同班
        if curent[1] == 'Y':
            last_class = last_class
        else:
            # 当前和上一个不同，切换班级，与上一个班级不同
            if last_class is c1:
                last_class = c2
            elif last_class is c2:
                last_class = c1

        last_class.append(int(curent[0]))

    c1.sort()
    c2.sort()
    print(*c1)
    print(*c2)


try:
    s = '1/N 2/Y 3/N 4/Y'
    # s = '6/N 2/Y 3/N 4/Y'
    s = '6/N 2/Y 3/N 4/Y 5/Y 8/N 9/N'
    s = '1/N 2/Y 3/N 4/Y 5/Y'
    data = s.split()
    main(data)
except:
    print('ERROR')
