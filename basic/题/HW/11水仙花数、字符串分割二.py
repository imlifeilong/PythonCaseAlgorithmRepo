def main(s):
    def ismod(string):
        num = sum(map(ord, string))
        if 100 > num or num > 999:
            return False
        x = num // 100  # 百
        y = num // 10 % 10  # 十
        z = num % 10  # 个
        return x * x * x + y * y * y + z * z * z == num

    def dfs(index, string, tmp):
        if not string:
            result.append(tmp.copy())
            return

        for i in range(len(string)):
            substr = string[:i + 1]
            # 判断如果符合
            if ismod(substr):
                # 记录符合的子串
                tmp.append(substr)
                # 接着判断剩下的部分
                dfs(index + 1, string[i + 1:], tmp)
                # 回溯
                tmp.pop()

    result = []
    dfs(0, s, [])
    print(result)
    if len(result) == 0:
        print(0)
    elif len(result) > 1:
        print(-1)
    elif len(result) == 1:
        print(len(result[0]))


s = 'abc'
s = 'AXdddF'
# s = "Gddd$Gdddf3@d5a8"
s = 'f3@d5a8'
main(s)
