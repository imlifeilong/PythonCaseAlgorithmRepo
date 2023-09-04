class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1

        maxlen = 0
        cache = []

        n = len(s)
        # 一趟一趟的扫描序列，每次选择一个位置开始向后扫，
        for i in range(n):
            # 从第i个位置开始向后扫描，找到[i:len(s))中最长的无重复的子串
            for j in range(i, n):
                tmp = s[j]
                # 将当前的值加到缓存里
                if tmp not in cache:
                    cache.append(tmp)
                else:
                    # 如果当前值，在缓存里，就说明已经重复了，此时缓存里的值就是没有重复的，求其长度
                    maxlen = max(maxlen, len(cache))
                    # 清空缓存，然后从下一个i位置重新开始
                    cache = []
                    break

        return maxlen


if __name__ == '__main__':
    """
    最长的没有重复的子串，就是这个子串里没有重复元素，子串是连续的
    以a开始的时候 (a) bcabcbb -> 最长的无重复的子串 (abc)abcbb
    以b开始的时候 a(b)cabcbb -> 最长的无重复的子串 a(bca)bcbb
    以c开始的时候 ab(c)abcbb -> 最长的无重复的子串 ab(cab)cbb
    ...
    以c开始的时候 abcab(c)bb -> 最长的无重复的子串 abcab(cb)b
    以b开始的时候 abcabc(b)b -> 最长的无重复的子串 abcabc(b)b
    以b开始的时候 abcabcb(b) -> 最长的无重复的子串 abcabcb(b)
    """
    s = 'abcabcbb'
    # s = 'bbbbb'
    s = "pwwkeswr"
    s = ''
    # s = ' '
    # s = 'au'
    # s = 'dvdf'
    obj = Solution()
    res = obj.lengthOfLongestSubstring(s)
    print(res)
