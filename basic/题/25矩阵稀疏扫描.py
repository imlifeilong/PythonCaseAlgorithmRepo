# row, col = map(int, input().split())


def max_continu_string(string, c='0'):
    """
    判断序列中连续字符串的个数
    :param string:
    :param c:
    :return:
    """
    length = len(string)
    count = 1
    res = 0
    for i in range(1, length):
        # 从s[1]开始 如果s[i] == s[i-1] count+1 否则 count 重置为1
        if string[i] == c and string[i] == string[i - 1]:
            count += 1
            res = max(count, res)
        else:
            count = 1

    return res


def main(data, col, row):
    row_0_count = 0
    col_0_count = 0
    # 构建矩阵保存
    col_tmp = [[] for _ in range(row)]

    row_mid = row // 2
    col_mid = col // 2
    for i in range(col):
        # 行中 连续的0的个数超过一半
        if max_continu_string(data[i]) > row_mid:
            row_0_count += 1

        # 将列转换成行
        for j in range(row):
            col_tmp[j].append(data[i][j])

    for h in range(row):
        # 列中 连续的0的个数超过一半
        if max_continu_string(col_tmp[h]) > col_mid:
            col_0_count += 1
    print(row_0_count)
    print(col_0_count)


col, row = 5, 3
s = """-1 0 1
0 0 0
-1 0 0
0 -1 0
0 0 0"""

col, row = 3, 3
s = """1 0 0
0 1 0
0 0 1
"""


data = [i.split() for i in s.split('\n')]
main(data, col, row)
