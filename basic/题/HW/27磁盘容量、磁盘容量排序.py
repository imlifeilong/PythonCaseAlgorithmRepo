import re


def main(data, n):
    result = []
    calls = {'M': lambda x: x, 'G': lambda x: x * 1024, 'T': lambda x: x * 1024 * 1024}
    for row in data:
        # 用正则 根据单位分割
        tmp = re.split('[MGT]', row)
        index = 0
        res = 0
        for s in tmp:
            if s == '':
                continue
            num = int(s)
            unit = row[index + len(s)]
            res += unit in calls and calls[unit](num)
            # if unit == 'M':
            #     res += num
            # elif unit == 'G':
            #     res += num * 1024
            # elif unit == 'T':
            #     res += num * 1024 * 1024
            # 调过当前值和单位的长度
            index += len(s) + 1
        result.append((row, res))

    for j in sorted(result, key=lambda x: x[1]):
        print(j[0])


s = """2G4M
3M2G
1T"""
s = """1G
1024M
2G"""
n = 3
data = s.split('\n')
main(data, n)
