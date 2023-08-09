def main(data):
    # 计算当前位置的上下左右中
    position = [(-1, 0), (0, -1), (0, 0), (0, 1), (1, 0)]
    row_len = len(data)
    col_len = len(data[0])
    res = 0
    for i in range(row_len):
        for j in range(col_len):
            for x, y in position:  # 当前位置 和 上 下 左 右 有1个位置停车了 就开监控
                _x = i + x
                _y = j + y
                if 0 <= _x < row_len and 0 <= _y < col_len and data[_x][_y] == '1':
                    res += 1
                    break
    print(res)


data = """0 0 0
0 1 0
0 0 0""".split('\n')
data = """1 0 0
0 1 0
0 0 0""".split('\n')
dataset = [row.split() for row in data]
# print(dataset)
main(dataset)
