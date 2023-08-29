"""
思路
1、先对所有的灯的高度进行排序，即对y1进行排序
2、第一次就将第一个元素作为基准值，并且找出和基准值一行的灯，同一行 就是两个灯高低差，不超过灯的半径
3、

"""

s = """1 0 0 2 2
2 6 1 8 3
3 3 2 5 4
5 5 4 7 6
4 0 4 2 6""".split('\n')

# n = int(input())
#
# a = []
# for i in range(n):
#     id, x1, y1, x2, y2 = map(int, input().split())
#     a.append(Node(id, x1, y1, x2, y2))

n = 5
a = []
for i in range(n):
    id, x1, y1, x2, y2 = map(int, s[i].split())
    a.append((id, x1, y1, x2, y2))

print(a)
# 第一次排序，按照高度从高往低排
a.sort(key=lambda x: x[2])

l = 0
for i in range(1, n):
    # 找到与基准灯在同一行的所有灯，高低偏差不超过灯半径的，算在同一行
    # 第i个灯的高度，和基准灯的高度，小于基准灯的半径，就属于同一行
    if a[i][2] - a[l][2] <= (a[l][4] - a[l][2]) / 2:
        continue

    # l到i的灯属于同一行，对这些灯进行排序，按行排序
    a[l:i] = sorted(a[l:i], key=lambda x: x[1])
    # 此时的第i个灯，已经属于下一行了，选为基准灯，然后再进行排序
    l = i

# 最后一个基准灯及其同行灯进行排序
a[l:] = sorted(a[l:], key=lambda x: x[1])

for i in range(n):
    print(a[i][0], end=' ')
