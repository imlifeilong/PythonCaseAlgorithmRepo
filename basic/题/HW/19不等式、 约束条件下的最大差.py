def main(s):
    data = s.split(';')
    a = [list(map(float, row.split(','))) for row in data[:3]]

    x = data[3].split(',')  # 系数
    b = data[4].split(',')  # 右值
    c = data[5].split(',')  # 不等式
    result = []
    status = True
    for i in range(len(a)):
        val = 0
        # 计算左值
        for j in range(len(a[i])):
            val += a[i][j] * int(x[j])
        # 计算左值和右值的差的绝对值
        target = float(b[i])
        sub = int(abs(val - target))
        # 根据不等式 判断左右值是否成立
        if c[i] == '<=':
            status = val <= target and status
            result.append(sub)
        elif c[i] == '>=':
            status = val >= target and status
            result.append(sub)
        elif c[i] == '>':
            status = val > target and status
            result.append(sub)
        elif c[i] == '<':
            status = val < target and status
            result.append(sub)
        elif c[i] == '=':
            status = val == target and status
            result.append(sub)
    # 打印结果和最大的差
    print(status, max(result))


s = '2.3,3,5.6,7,6;11,3,8.6,25,1;0.3,9,5.3,66,7.8;1,3,2,7,5;340,670,80.6;<=,<=,<='
s = '2.36,3,6,7.1,6;1,30,8.6,2.5,21;0.3,69,5.3,6.6,7.8;1,13,2,17,5;340,67,300.6;<=,>=,<='
main(s)
