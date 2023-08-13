"""
黑板上已经写上了N个正整数
同学们需要给这每个数分别上一种颜色
为了让黑板报既美观又有学习意义
老师要求同种颜色的所有数都可以被这个颜色中最小的那个数整除
现在帮小朋友们算算最少需要多少种颜色，给这N个数进行上色


输出只有一个整数，为最少需要的颜色种数
输入
3
2 4 6
输出
1
说明：
所有数都能被2整除

输入
4
2 3 4 9
输出
2
说明：
2与4涂一种颜色，4能被2整除
3与9涂另一种颜色，9能被3整除
不能涂同一种颜色

"""


def tuyanse_while(knums):
    res = 0
    # for i in range(len(knums)):
    #     mink = knums[i]
    # for mink in knums:
    #     i = knums.index(mink)

    length = len(knums)
    i = 0
    while i < length:
        mink = knums[i]

        j = i + 1
        while j < len(knums):
            if knums[j] % mink == 0:
                knums.pop(j)
            else:
                j += 1
        length = len(knums)
        i += 1
    print(len(knums))


def tuyanse_for(knums):
    for mink in knums:
        i = knums.index(mink)

        j = i + 1
        while j < len(knums):
            if knums[j] % mink == 0:
                knums.pop(j)
            else:
                j += 1

    print(len(knums))


k = [2, ]
# k = [2, 3]
k = [2, 4, 6]
k = [2, 3, 4, 9]

tuyanse_for(k)
tuyanse_while(k)
