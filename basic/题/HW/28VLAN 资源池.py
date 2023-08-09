def main(s, n):
    data = s.split(',')
    tmp_list = []
    for c in data:
        if '-' in c:
            row = list(map(int, c.split('-')))
            row_list = list(range(row[0], row[1] + 1))
            tmp_list.extend(row_list)
        else:
            tmp_list.append(int(c))
    tmp_list.sort()
    n in tmp_list and tmp_list.remove(n)

    result = []

    # 开始值和上一个值都为第一值
    start = end = tmp_list[0]

    for i in range(1, len(tmp_list)):
        if tmp_list[i] == end + 1:
            end = tmp_list[i]  # 如果当前值比前一个值大1，继续进行对比
        else:
            # 如果当前值和前一个值不连续，差值大于1
            # 如果有一个数，前后不连续，开始和结束值相同
            if start == end:
                result.append(str(start))
            else:
                result.append(f'{start}-{end}')
            start = end = tmp_list[i]

    if start == end:
        result.append(str(start))
    else:
        result.append(f'{start}-{end}')
    print(','.join(result))


s = '20-21,15,18,30,5-10'
n = 15

# s = '1-5'
# n = 2

s = '5,1-3'
n = 10

main(s, n)
