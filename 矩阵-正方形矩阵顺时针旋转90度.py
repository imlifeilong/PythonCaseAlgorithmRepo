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
    while a <= b:
        for i in range(a, b):
            matrix[a][c+i], matrix[a+i][d], matrix[b][d-i], matrix[b-i][c] \
            = matrix[b-i][c], matrix[a][c+i], matrix[a+i][d], matrix[b][d-i]
        a = c = a + 1
        b = d = b - 1
    for x in matrix:
        print(x)

if __name__ == '__main__':
    matrix = [                  
        [1, 2, 3, 4, 5, 6],         # 0
        [11, 12, 13, 14, 15, 16],   # 1
        [21, 22, 23, 24, 25, 26],   # 2
        [31, 32, 33, 34, 35, 36],   # 3
        [41, 42, 43, 44, 45, 46],   # 4
        [51, 52, 53, 54, 55, 56],   # 5
    ]
    '''
    第一轮打印
    1, 2, 3, 4, 5, 6
    11             16
    21             26
    31             36
    41             46
    51,52,53,54,55,56


    '''
    _print_matrix(matrix)