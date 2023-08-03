"""
几个卡片中的数字，组成的最大数

"""


def main(data):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if int(data[i] + data[j]) < int(data[j] + data[i]):
                data[i], data[j] = data[j], data[i]
    print(''.join(data))


s = '22,221'
s = '4589,101,41425,9999'
data = s.split(',')
main(data)
