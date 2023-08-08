def main(s, t):
    target_len = len(t)
    # len(s) - target_len + 1 最后一位不越界
    for i in range(len(s) - target_len + 1):
        tmp = s[i:i + target_len]
        if tmp == t:
            print(i + 1)
            return
    print('No')


s = """AVERDXIVYERDIAN"""
t = "RDXI"
main(s, t)
