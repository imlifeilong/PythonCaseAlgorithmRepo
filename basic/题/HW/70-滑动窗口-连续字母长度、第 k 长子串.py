def main(s, k):
    res = {}

    # 变成while循环，优化索引移动位置
    for i in range(len(s)):
        # 找到当前值连续长度
        j = i + 1
        while j < len(s):
            if s[i] == s[j]:
                j += 1
            else:
                break
        curlen = j - i

        # 记录长度
        if s[i] in res:
            if res[s[i]] < curlen:
                res[s[i]] = curlen
        else:
            res[s[i]] = curlen

    result = sorted(res.values(), reverse=True)
    if k <= len(result):
        print(result[k - 1])
    else:
        print(-1)


def process(s, k):
    n = len(s)
    left = 0
    right = 0
    cache = {}

    while right < n - 1:
        tmp = s[left]
        # right下一位 如果与当前left所指的值一样，则继续移动right

        if s[right + 1] == tmp:
            right += 1
        else:
            # 如果不相同，记录窗口的长度，并且判断该字母之前是否出现过，
            # 如果出现过，则取当前值和之前值之间较大的，重新记录
            cache[tmp] = max(right - left + 1, cache.get(tmp, 0))
            right += 1  # right继续移动
            left = right  # left追上right后，重新开始

    # 因为循环退出条件是right<总长度-1，所以最后一段需要单独计算
    if right == n - 1 and s[left] == s[right]:
        cache[s[left]] = max(right - left + 1, cache.get(s[left], 0))

    result = sorted(cache.values(), key=lambda x: -x)
    if len(result) >= k:
        print(result[k - 1])
    else:
        print(-1)


s = 'AAAAHHHBBCDHHHH'
k = 3

# s = 'AABAAA'
# k = 2
# s = 'ABCCB'
# k = 4

# s = 'ABC'
# k = 4
main(s, k)
process(s, k)
