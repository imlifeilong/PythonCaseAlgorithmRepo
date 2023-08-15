def main(s):
    asc = [ord(x) for x in s]
    left = 0
    right = len(s) - 1

    # 假设两个分割点 的字母分别是z，以z分割
    # ascii值的总和 去掉较大的两个值，然后再平分三份
    begin = (sum(asc) - 122 * 2) // 3
    # 以a为分割点，去掉最小的两个值 然后再平均分三份
    end = (sum(asc) - 97 * 2) // 3

    left_val = 0
    right_val = 0
    res = 0, 0
    # 左值的和不能大于第二个分割点的值
    while left_val < end + 1:
        left_val += asc[left]
        left += 1
        # 当左边的值到达begin时，再处理右边的
        if left_val >= begin:
            while right_val < end:
                right_val += asc[right]
                right -= 1
                # 左 右 中间的值 都相等，并且左 右 中 没有相交
                if right_val == left_val == sum(asc[left + 1:right]) and left <= right:
                    res = left, right
                    break
            else:
                continue
            break
    print(*res)


s = 'aabaacaa'
s = 'abacd'
main(s)
