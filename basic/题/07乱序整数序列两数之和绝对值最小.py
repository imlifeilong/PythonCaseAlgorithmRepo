"""
找到数组中两个数，绝对值最小
-1 -3 7 5 11 15
-3 5 2
"""

import sys

print(sys.maxsize)


def main(data):
    minsum = sys.maxsize
    result = None
    for i in range(len(data) - 1):
        for j in range(i + 1, len(data) - 1):
            mintmp = abs(data[i] + data[j])
            if abs(data[i] + data[j]) < minsum:
                minsum = mintmp
                result = (data[i], data[j])
    print(*result, minsum)


s = list(map(int, '-1 -3 7 5 11 15'.split()))
print(s)
main(s)
