"""
删除数字中k个数，使得结果的数值最小
"""


def main(data, k):
    stack = []
    for i in data:
        # 栈里的数据如果比当前的值大，则出栈
        while stack and stack[-1] > i and k > 0:
            stack.pop()
            k -= 1
        stack.append(i)
    # 去除首个字符为0 的情况
    print(''.join(stack[:len(stack) - k]).lstrip('0') or '0', k)


s = '10200'
k = 1
# s = '123456'

main(s, k)
