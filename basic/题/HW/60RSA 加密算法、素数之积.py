def is_prime(num):
    # 判断是否是素数
    if num <= 1:
        return False
    # 2 到 平方根之间 找到能否被整除的数，如果没有就是素数
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def main(num):
    for i in range(2, num):

        # 找到第一个能被num整除的素数，整除的结果也是素数
        if is_prime(i) and num % i == 0 and is_prime(num // i):
            return i, num // i

    return -1, -1


def result(num):
    factors = set()  # 使用集合进行去重
    tmp = num  # 用tmp保存num的副本，方便后面进行计算
    f = 2  # 最小质数从2开始。要记得这个方法。
    while tmp != 1:
        if tmp % f != 0:
            f += 1  # 如果tmp不能被f整除，尝试下一个更大的f
        else:
            # 将找到的因数f添加到factors集合中
            factors.add(f)
            tmp //= f  # 除以因数f，更新tmp的值，去除重复的因数

    for i in factors:
        for j in factors:
            # 如果两个数相乘要等于num
            if i * j == num:
                min_factor = min(i, j)
                max_factor = max(i, j)
                return (f"{min_factor} {max_factor}")
    # 没有找到
    return "-1, -1"


n = 15151511
res = main(n)
#
print(*res)

import time

st = time.time()
res = result(n)
print(res)
print(time.time() - st)
