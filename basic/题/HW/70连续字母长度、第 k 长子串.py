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


s = 'AAAAHHHBBCDHHHH'
k = 3

s = 'AABAAA'
k = 2
s = 'ABC'
k = 4
main(s, k)
