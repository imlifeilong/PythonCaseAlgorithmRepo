def main(data):
    stack = []
    maxlen = float('-inf')
    for c in data:
        if c.isdigit():
            if stack and c >= stack[-1]:
                stack.append(c)
            elif not stack:
                stack.append(c)
            else:
                maxlen = max(len(stack), maxlen)
                stack = []
        else:
            maxlen = max(len(stack), maxlen)
            stack = []
    print(maxlen)


s = list('abc2234019A334bc')
main(s)
