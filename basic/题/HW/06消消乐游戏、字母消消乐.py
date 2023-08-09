"""
一段字符串中遇见相邻的两个字符串，就消除，反复消除，直到无法消除为止

"""


def start(data):
    stack = []

    for i in data:
        # 如果当前元素与栈顶元素相同，出栈
        if stack and stack[-1] == i:
            stack.pop()
        else:
            # 如果不同则入栈
            stack.append(i)
    print(stack)
    return ''.join(stack)


s = 'mMbccbc'
# s = 'gg'
start(s)
