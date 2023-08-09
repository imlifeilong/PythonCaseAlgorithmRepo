def main(data):
    res = 0
    index = 0
    while len(data) > index:
        if data[index] == 0:
            # 判断前一个位置是否是0， 第一位不用判断
            _prev = index == 0 or data[index - 1] == 0
            # 判断下一个位置是否是0， 最后一位不用判断
            _next = index == len(data) - 1 or data[index + 1] == 0
            # 前后都位0的时候可以坐人
            if _prev and _next:
                index += 1
                res += 1
        index += 1
    print(res)


s = '1,0,0,0,1'.split(',')
s = '0,0,1,0,0,1,0,0,0,1'.split(',')
s = '0,0,0,0,0'.split(',')
s = '1,0,0,1'.split(',')
data = list(map(int, s))
main(data)
