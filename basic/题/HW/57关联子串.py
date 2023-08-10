def main(s1, s2):
    def dfs(index, s, tmp, result):

        if index == len(s):
            # s1全排列的一种，是否在s2种
            res = s2.find(''.join(tmp))
            res != -1 and result.append(res)
            return res

        for c in s:
            # 对s1进行无重复的全排列
            if c in tmp:
                continue
            tmp.append(c)
            dfs(index + 1, s, tmp, result)
            # 回溯
            tmp.pop()

    result = []
    dfs(0, s1, [], result)
    if result:
        result.sort()
        print(result[0])
    else:
        print('-1')


s1 = 'abc'
s2 = 'eabcafghicabiiiacb'
# s2 = 'efghicaibii'
main(s1, s2)
