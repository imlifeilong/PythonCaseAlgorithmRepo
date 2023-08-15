def main(data):
    left = []
    right = []
    for x in data:
        if x > 0:
            left.append(x)
        else:
            right.append(abs(x))

    while left and right:
        # 根据题意 左右各出一个人
        left_top = left.pop()
        right_top = right.pop()

        subval = left_top - right_top
        # 左边 体力 大于 右边， 左边的胜利，进入队列和下一个人继续pk
        if subval > 0:
            left.append(subval)

        elif subval < 0:
            right.append(subval * -1)
    print(len(left) + len(right))


s = '5 10 8 -8 -5'.split()
data = list(map(int, s))
main(data)
