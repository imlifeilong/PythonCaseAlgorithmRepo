def parse(n, m, data, per):
    # n 批人
    # m 库存
    # data 每批消费
    # per 单位时间内生成
    for i in range(n):
        # 消费
        m -= data[i]
        # 每次消费完后 判断是否库存还够
        if m < 0:
            return False
        # 消费完后 生成
        m += per
    return True


def main(n, m, data):
    # 找到一个较小的生产值，满足每批人来不需要排队
    left = 0  # 可取的最小值
    right = max(data)  # 最大值
    # 使用二分法找到 0 和 max 之间找到最小的值
    while left < right:
        mid = (left + right) // 2
        if parse(n, m, data, mid):
            right = mid - 1
        else:
            left = mid + 1
    print(left)


n = 3
m = 14
data = list(map(int, '10 4 5'.split()))
main(n, m, data)
