def main(data, n):
    data.sort()  # 排序
    count = 0
    left = 0
    rigth = len(data) - 1
    while left < rigth:
        # 找到单个大于能力值的人， 最右遍的大，所以从右向左比较
        if data[rigth] >= n:
            rigth -= 1
            count += 1
        # 找到两个大于能力值的人
        elif data[rigth] + data[left] >= n:
            left += 1
            rigth -= 1
            count += 1
        else:
            left -= 1
    print(count)


n = 8
s = '3 1 5 7 9'.split()
s = '3 1 5 7 9 2 6'.split()
data = list(map(int, s))
main(data, n)
