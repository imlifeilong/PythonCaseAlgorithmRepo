def main(data):
    length = len(data)
    maxval = 0
    for i in range(length):
        for j in range(i + 1, length):
            # 计算边长为 data[i] data[j]矩形面积
            area = min(data[i], data[j]) * (j - i)
            maxval = max(maxval, area)  # 找当比较大的面积

    print(maxval)


def main1(data):
    # 双指针
    left = 0
    right = len(data) - 1
    maxval = 0
    while left < right:
        if data[left] > data[right]:
            area = data[right] * (right - left)
            right -= 1
        else:
            area = data[left] * (right - left)
            left += 1
        maxval = max(maxval, area)
    print(maxval)


s = '10,9,8,7,6,5,4,3,2,1'.split(',')
data = list(map(int, s))
main(data)
main1(data)
