"""
31
32 01 00 AE 90 02 00 01 02 30 03 00 AB 32 31 31 02 00 32 33 33 01 00 CC
tag 32 长度 01 00（小端序表示为1）  值 AE
tag 90 长度 02 00（小端序表示为2）  值 01 02
tag 30 长度 03 00（小端序表示为3）  值 AB 32 31
tag 31 长度 02 00（小端序表示为2）  值 32 33
tag 33 长度 01 00（小端序表示为1）  值 CC


存储 12345678
大端 12 34 56 78
小端 78 56 34 12
"""


def main(data, target):
    data = data.split()
    p = 0
    while p < len(data):
        tag = data[p]
        length_bytes = data[p + 1:p + 3]
        length = int(''.join(length_bytes[::-1]), 16)
        if tag == target:
            value = data[p + 3:p + 3 + length]
            print(' '.join(value))
        p += (1 + 2 + length)


s = '32 01 00 AE 90 02 00 01 02 30 03 00 AB 32 31 31 02 00 32 33 33 01 00 CC'
target = '31'

main(s, target)
