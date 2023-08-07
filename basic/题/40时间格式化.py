def main(data):
    data.sort(key=str2int)
    for row in data:
        print(row)


def str2int(text):
    tmp = text.split(':')
    h = int(tmp[0]) * 60 * 60 * 1000  # 小时转换毫秒
    m = int(tmp[1]) * 60 * 1000  # 分钟转换毫秒
    stmp = tmp[2].split('.')
    s = int(stmp[0]) * 1000  # 秒转换毫秒
    ms = int(stmp[1])
    return h + m + s + ms


s = """01:41:8.9
1:1:09.211"""

s = """22:41:08.023
22:41:08.23"""

s = """23:41:08.023
1:1:09.211
08:01:22.0"""

data = s.split('\n')
main(data)
