"""
给定一个字符串的摘要算法，请输出给定字符串的摘要值
1.去除字符串中非字母的符号。
2.如果出现连续字符(不区分大小写),则输出：该字符(小写)+连续出现的次数。
3.如果是非连续的字符(不区分大小写),则输出：该字符(小写)+该字母之后字符串中出现的该字符的次数
4.对按照以上方式表示后的字符串进行排序：字母和紧随的数字作为一组进行排序，数字大的在前，
  数字相同的，则按字母进行排序，字母小的在前。

思路：
首先统计字符串中各个字母出现的次数 记录在count中
使用滑动窗口记录连续字母的个数，窗口的长度就是连续字母的个数

如果字母是非连续的，就需要统计当前位置之后，该字母出现的次数，
所以处理每个字母时，就先将该字母的个数-1，即count[tmp]-1 表示该字母在之后出现的次数

遇到非连续的字母，就直接获取count中该字母的个数
"""


def main(s):
    def counter(s):
        cache = {}
        for c in s:
            if c not in cache:
                cache[c] = 1
            else:
                cache[c] += 1
        return cache

    s1 = [c for c in s.lower() if c.isalpha()]
    # 统计字符串中每个字母的个数
    count = counter(s1)
    # 处理结尾
    s1.append('#')
    count['#'] = 1

    n = len(s1)
    left = 0
    right = 0
    result = []
    # 因为每次使用right+1进行判断，为了防止越界，终点使用n-1，但是为了保证所有的字母都被扫到，所以结尾使用#
    # 这样就保证了right+1能指向最后一个字母
    # abcde n=5 right<4 最大只能到3 即到d, 字母e需要单独处理
    # abcde# n=6 right<5 最大到4 即e，这样就可以保证所有字母被扫到
    # 猜想 计算机中的字符串都是以\n结尾，也是为了好处理
    while right < n - 1:
        # 当前值tmp就是left指向的字母
        tmp = s1[left]
        # 当前字母的个数-1
        count[tmp] -= 1
        # 因为left 和right都是从0开始的，所以每次比较 right+1指向的字母和left指向的字母 是否相同，、
        # 如果相同就移动right
        if s1[right + 1] == tmp:
            right += 1
        else:
            # 如果不相同，计算当前窗口的长度，就是当前字母的个数
            tmp_length = right + 1 - left
            # tmp_length 如果大于1说明是连续的，则保存当前字母的个数
            # 如果不连续，则需要保存当前字母，在之后字符串中出现的次数 即count[tmp]
            result.append([tmp, tmp_length if tmp_length > 1 else count[tmp]])
            # 不相同了必须移动 left， 因为每次使用right+1进行比较，所以移到right+1，并且移动right
            left = right + 1
            right += 1
    # 对统计进行排序，(-x[1],x[0]) 对第二个字段进行逆序，第一个字段顺序
    result.sort(key=lambda x: (-x[1], x[0]))
    res = ''.join(map(lambda x: x[0] + str(x[1]), result))
    print(res)


s = 'bAaAcBb'
s = 'aabbcc'
main(s)
