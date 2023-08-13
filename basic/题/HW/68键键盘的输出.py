def main(s):
    screen = []
    tmp = []
    ctrla = False  # 是否全选
    # 1 输入 a
    # 2 复制所选字符 到剪切板
    # 3 剪切算选字符 到剪切板
    # 4 将剪切板的字符 粘贴到屏幕
    # 5 选中所有屏幕上的字符

    for c in s:
        # 没有全选的情况下，输入a
        if c == '1':
            # 全选的情况下
            if ctrla:
                screen.clear()
                ctrla = False
            screen.append('a')

        # 有选择字符的情况下，屏幕的字符放到剪切板中
        elif c == '2' and ctrla:
            tmp.clear()
            tmp.extend(screen)
        # 将屏幕的字符 剪切到剪切板
        elif c == '3' and ctrla:
            tmp.clear()
            tmp.extend(screen)
            screen.clear()
            ctrla = False
        elif c == '4':
            # 屏幕有选中的情况，覆盖粘贴
            if ctrla:
                screen.clear()
                screen = tmp
            else:
                # 没有选中 粘贴到后面
                screen.extend(tmp)
            ctrla = False
        elif c == '5':
            ctrla = True

    print(len(screen))


s = '1 1 5 1 5 2 4 4'.split()
# s = '1 1 1'.split()
main(s)
