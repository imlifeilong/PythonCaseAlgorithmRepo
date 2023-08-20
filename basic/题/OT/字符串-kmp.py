'''
KMP:给定两个字符串src和des，长度分别为N和M。实现一个算法，
如果字符串src中含有子串des，则返回des在src中的开始位置，不含有则返回-1

next 数组存 每个字符之前 字符串 前缀 后缀 最长的匹配长度

'''
class KMP():
    def _next(self, string):
        string_length = len(string)
        if string_length == 1:
            return [-1]

        tmp = [0] * string_length
        # next中第一位规定为-1,第二位 0
        tmp[0], tmp[1] = -1, 0
        # 数组的索引
        index = 2
        # 上一个元素 之前 的字符串，前缀，后缀 最长的重复子串长度
        # 上一个元素的 之前的字符串，前缀匹配 最后一位的位置
        current = 0

        while index < string_length:
            # 如果 当前字符之前的一位 与 上一趟 前缀匹配最后一个位置的字符相同
            if string[index-1] == string[current]:
                # 匹配的位置 增加1位
                current += 1
                # 当前位置的next值
                tmp[index] = current
                index += 1

            # 如果不匹配，该元素之前的 匹配也为0，该元素也为0
            elif current == 0:
                tmp[index] = 0
                index += 1
            else:
                current = tmp[current]
        return tmp

    def mapping(self, src, des):
        if not src or not des or len(src) < len(des):
            return -1

        next_table = self._next(src)
        si, di = 0, 0

        while si < len(src) and di < len(des):
            if src[si] == des[di]:
                si += 1
                di += 1
            elif di == 0:
                si += 1
            else:
                di = next_table[di]

        return -1 if di != len(des) else si - di

if __name__ == '__main__':
    s = 'abcdechfac'
    d = 'dec'
    kmp = KMP()
    res = kmp.mapping(s, d)
    print(res)