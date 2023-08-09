def main(m, n):
    res = 0
    for i in range(n):
        row = m[i]
        max_num = float('-inf')  # 标注最大值为负无穷
        for j in range(n):
            # 开始移动
            row.append(row.pop(0))
            # 计算移动后的值
            bin_text = int(''.join(row), 2)
            # 取比较大的值
            max_num = max(bin_text, max_num)
        # 第i行的最大值
        # print(i, max_num)
        res += max_num
    print(res)


n = 5
m = list(map(lambda x: x.split(','), """1,0,0,0,1
0,0,0,1,1
0,1,0,1,0
1,0,0,1,1
1,0,1,0,1""".split('\n')))
# print(m)
main(m, n)
