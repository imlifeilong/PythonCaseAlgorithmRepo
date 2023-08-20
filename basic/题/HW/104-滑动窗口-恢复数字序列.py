def main(s, w):
    def counter(string):
        cache = {}
        for c in string:
            if c in cache:
                cache[c] += 1
            else:
                cache[c] = 1
        return cache

    # 统计个数字的个数
    base = counter(s)

    # 固定的滑动窗口，比较窗口内的元素 与 base 相同
    for i in range(1000 - w):
        tmp = map(str, range(i, i + w))
        tmp_counter = counter(''.join(tmp))

        if tmp_counter == base:
            print(i)
            break


s = '19801211'
w = 5

s = '432111111111'
w = 4
main(s, w)
