def main(s):
    maxval = 0
    for i in range(len(s)):
        print(s[i])
        if s[i] == '1':
            continue

        # 当前位置到左边的 所有连续的空闲位置
        left = 0
        for j in range(i):
            if s[j] == '1':
                left = j

        # 当前位置到右边的 所有连续的空闲位置
        right = 0
        for h in range(i, len(s)):
            if s[h] == '1':
                right = h
                break

        # 计算当前位置 左 右停车的距离，取左右距离中最近的一个
        tmp = min(i - left, right - i)
        # 找到所有最近距离中，最大的一个
        maxval = max(maxval, tmp)
    print(maxval)


s = '1,0,0,0,0,1,0,0,1,0,1'.split(',')
# 说明 当停在第2位置 最近就是 1
# 停在3 最近2 1到3
# 停在4 最近2 4到6
#

main(s)
