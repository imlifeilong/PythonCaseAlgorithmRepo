def main(s):
    res = 0, 0

    index = 0
    maxval = 0
    while index < len(s):
        subtext = s[index:]
        # 找到括号左 右 边界，并且找到括号中的值
        left = subtext.find('(')
        right = subtext.find(')')
        # 没有括号，直接跳出
        if left == -1:
            break
        tmp = subtext[left + 1:right]
        x, y = tmp.split(',')
        # 找到距离最远的
        if not (x.startswith('0') or y.startswith('0')):
            x = int(x)
            y = int(y)
            if maxval < x * x + y * y:
                res = x, y
        # 索引跳过当前的括号
        index = index + right + 1
    print(res)


s = 'ferg(3,10)a13fdsf3(3,4)f2r3rfasf(5,10)'
s = 'asfefaweawfawf(0,1)fe'
s = 'asfefaw(01,10)eawfawf(0,1)fe'
main(s)
