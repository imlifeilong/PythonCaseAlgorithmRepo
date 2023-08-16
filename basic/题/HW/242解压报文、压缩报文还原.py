'''
力扣 394. 字符串解码

'''
def main(s):
    stack = []
    for c in s:
        # 遇见]出栈
        if c == ']':
            # 先获取[之后 ]之前的，即[]中间的字符
            tmpstr = []
            while stack and stack[-1] != '[':
                # insert 0 是因为栈是先入后出的
                tmpstr.insert(0, stack.pop())

            # 弹出 [
            stack.pop()
            print(stack, tmpstr)
            # 处理数字，十位数 或者百位数 更高位
            tmpnum = []
            while stack and stack[-1].isdigit():
                tmpnum.insert(0, stack.pop())

            num = int(''.join(tmpnum))
            strs = ''.join(tmpstr)
            # 计算字符的长度
            tmp = strs * num
            stack.extend(list(tmp))
        else:
            stack.append(c)
    print(''.join(stack))


s = '3[m2[c]]'
main(s)
