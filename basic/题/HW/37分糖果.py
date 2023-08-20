"""
5 -1 = 4
4/2=2
2/2=1

5+1=6
6/2=3
3-1=2 3+1=4
2/2=1 4/2=2
      2/2=1

"""


def main(n):
    count = 0
    while n != 1:
        # # 剩下3个糖时，先放回1个，再平均分一次，所以要2次操作
        if n == 3:
            count += 2
            break
        if n % 2 != 0:
            # 奇数-1 次数小于等于 奇数+1
            # 当前的数平分后，如果是奇数就-1 偶数就+1
            if (n + 1) // 2 % 2 == 0:
                n += 1
            else:
                n - 1
            count += 1

        n //= 2
        count += 1
    print(count)


def process(n):
    # 当前的数为1时就可以退出了
    if n == 1:
        return 0
    # 当前的数可以平分，就直接平分后再进行下一步操作
    if n % 2 == 0:
        return process(n // 2) + 1
    # 如果不能平分，可以右两种操作
    # 当前的数加1，再进行下一个操作
    p1 = process(n + 1) + 1
    # 当前的数减1 再进行下一个操作 每次操作后 操作次数都要加1
    p2 = process(n - 1) + 1
    return min(p1, p2)


def process_cache(n, cache):
    # 加缓存
    if n in cache:
        return cache[n]

    if n == 1:
        cache[n] = 0
    elif n % 2 == 0:
        cache[n] = process_cache(n // 2, cache) + 1
    else:
        cache[n] = min(process_cache(n + 1, cache), process_cache(n - 1, cache)) + 1

    return cache[n]


import time

n = 60001012101123
# n = 5
# n = 15
st = time.time()
main(n)
print(time.time() - st)
st = time.time()
res = process(n)
print(time.time() - st)
print(res)
cache = {}
st = time.time()
res = process_cache(n, cache)
print(time.time() - st)
print(res)
