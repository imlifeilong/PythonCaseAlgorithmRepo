import math


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# def is_prime(num):
#     if num <= 1:
#         return False
#     if num <= 3:
#         return True
#     if num % 2 == 0 or num % 3 == 0:
#         return False
#
#     for i in range(5, int(math.sqrt(num)) + 1, 6):
#         if num % i == 0 or num % (i + 2) == 0:
#             return False
#
#     return True


for i in range(100):
    if is_prime(i):
        print(i)
