def main(data):
    # 要存下n个文件，最少可能需要1个光盘，最多可能需要n个光盘

    def process1(data):
        # 双循环 时间复杂度 O(N^2)
        n = len(data)

        minval = float('inf')

        # 用遍历的方式找到一个最小的光盘数（可以使用二分法加速）
        for i in range(n, 0, -1):
            # 有i个光盘
            boxs = [500] * i
            isok = True
            for j in range(n):
                # 每次找较大的装
                boxs.sort()
                # print(boxs, data[j])
                # 当前的光盘能否装下，如果能装下 则继续装下一个
                if boxs[i - 1] >= data[j]:
                    boxs[i - 1] -= data[j]
                # 如果装不下，就说明光盘数量不够
                else:
                    isok = False
                    break
            # 找到最小的光盘数
            if isok:
                minval = min(i, minval)
        print(minval)

    def process2(data):
        # 二分法 + 循环 时间复杂度 O(N*log(N))
        n = len(data)
        left = 0
        right = len(data) - 1

        while left <= right:
            mid = (left + right) // 2
            # 光盘
            boxs = [500] * mid
            isok = True
            for j in range(n):
                # 每次找较大的装
                boxs.sort()
                # print(boxs, data[j])
                # 当前的光盘能否装下，如果能装下 则继续装下一个
                if boxs[mid - 1] >= data[j]:
                    boxs[mid - 1] -= data[j]
                # 如果装不下，就说明光盘数量不够
                else:
                    isok = False
                    break
            if isok:
                right = mid - 1
            else:
                left = mid + 1
        print(left)

    data.sort(reverse=True)

    process1(data)
    process2(data)


s = '100,100,200,300'.split(',')
s = '100,500,300,200,400'.split(',')
data = list(map(int, s))
main(data)
