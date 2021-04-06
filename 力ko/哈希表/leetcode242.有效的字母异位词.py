'''
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        mapping = {}
        for i in s:
            if i not in mapping:
                mapping[i] = 0
            mapping[i] += 1
        for j in t:
            if j in mapping:
                mapping[j] -= 1

        for k, v in mapping.items():
            if v > 0:
                return False
        return True


if __name__ == '__main__':
    so = Solution()
    s = 'anagram'
    t = 'nagaram'
    print(so.isAnagram(s, t))
