"""
n-m中的勾股数
"""
import math


def coprime(a, b):
    """
    判断两个数是否互质
    :param a:
    :param b:
    :return:
    """
    while b:
        a, b = b, a % b
    return a == 1


def main(n, m):
    def _coprime(a, b):
        return True if math.gcd(a, b) == 1 else False

    count = 0
    for i in range(n, m):
        for j in range(i + 1, m):
            for h in range(j + 1, m):
                if i ** 2 + j ** 2 == h ** 2 and coprime(i, j) and coprime(i, h) and coprime(j, h):
                    print(f'{i} {j} {h}')
                    count += 1
    if count == 0:
        print('Na')


n = 5
m = 10
main(n, m)
# coprime(6, 8)
