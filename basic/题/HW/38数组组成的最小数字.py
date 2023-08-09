"""
数组组成的最小值
"""


def main(data):
    data = [int(i) for i in data]
    data.sort()
    print(data)
    data_str = [str(i) for i in data[:3]]
    data_str.sort()
    print(''.join(data_str))


s = '21,30,62,5,31'
s = '5,21'
data = s.split(',')
main(data)
