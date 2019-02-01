'''
'''


def _print_matrix(matrix):
    # a b 行 
    # c d 列
    # 左上第一个节点的位置(a, c)
    # 右下最后一个节点位置(b, d)
    a = c = 0
    b = len(matrix) - 1
    d = len(matrix[0]) - 1

    while a <= b and c <= d:
        if a == b:
            for i in range(c, d+1):
                print(matrix[a][i], end=',')
        elif c == d:
            for i in range(a, b+1):
                print(matrix[i][c], end=',')
        else:
            # 从第一列向右打印
            for i in range(c, d):
                print(matrix[a][i], end=',')
            # 从最后一列向下打印
            for i in range(a, b):
                print(matrix[i][d], end=',')
            # 从最后一列向左打印
            for i in range(d, c, -1):
                print(matrix[b][i], end=',')
            # 从最后行向上打印
            for i in range(b, a, -1):
                print(matrix[i][c], end=',')

        # 一轮打印完了，左上点向右下移动
        a += 1
        b -= 1
        #  右下点向左上移动
        c += 1
        d -= 1


if __name__ == '__main__':
    matrix = [
        # 0 1 2 3 4 5                   
        [1, 2, 3, 4, 5, 6],         # 0
        [11, 12, 13, 14, 15, 16],   # 1
        [21, 22, 23, 24, 25, 26],   # 2
        [31, 32, 33, 34, 35, 36],   # 3
        [41, 42, 43, 44, 45, 46],   # 4
        [51, 52, 53, 54, 55, 56],   # 5
        [61, 62, 63, 64, 65, 66]    # 6
    ]
    '''
    第一轮打印
    1, 2, 3, 4, 5, 6
    11             16
    21             26
    31             36
    41             46
    51             56
    61,62,63,64,65,66

    '''
    _print_matrix(matrix)