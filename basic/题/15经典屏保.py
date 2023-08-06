W, H = 800 - 50, 600 - 25


# w, h = W - 50, H - 25


def main(data):
    ws, hs = 1, 1

    w, h, t = data
    # 1秒移动一次，移动t次
    for i in range(t):
        # w h 方向各移动1位
        w += ws
        h += hs
        # 当有碰触到边界后，向相反方向移动
        if w == 0 or w == W:
            ws *= -1
        if h == 0 or h == H:
            hs *= -1
    print(w, h)


s = '0 0 10'.split()
# s = '500 570 10'.split()
data = [int(i) for i in s]
main(data)
# print(data)
