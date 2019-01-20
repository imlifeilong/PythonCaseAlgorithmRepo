# _*_ coding:utf-8 _*_
'''
第一个不重复的字符：adddwabbccdff中的w, google中的l
'''

class Handle:
    def __init__(self):
        self.duplicate = []

    def run(self, string):
        slen = len(string)
        if slen == 0:
            print "The string is empty"
        elif slen == 1:
            print "First unduplicated char is %s" % string
            return string
        for i in range(1, slen):
            #获取每个字符的位置
            char = string[i-1:i]
            #判断字符在该字符所在位置到字符尾部中出现，并且不在重复列表中，就追加到重复列表中，然后继续遍历
            if char in string[i:] and char not in self.duplicate:
                self.duplicate.append(char)
                continue
            #不在该字符所在位置到字符尾部中出现，也不在重复字符列表中
            elif char not in self.duplicate:
                print "First unduplicated char is %s" % char
                return char


if __name__ == "__main__":
    str1 = ""
    #str2 = "adddwabbccdff"
    str3 = "a"
    t = Handle()
    t.run(str1)
    #t.run(str2)
    t.run(str3)

    