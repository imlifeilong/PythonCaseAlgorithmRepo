'''
找到海量数据中前K大的数据
'''


class Solution(object):

    def buil_heap(self, data, index):
        # 建立小根堆
        root = int((index - 1) / 2)
        while data[index] < data[root]:
            data[index], data[root] = data[root], data[index]
            index = root
            root = int((index - 1) / 2)

    def heapify(self, data, index, length):
        # 调整堆
        left = index * 2 + 1
        while left < length:
            right = index * 2 + 2
            # 找出子节点中的最小值，替换
            minner = right if (right < length and data[right] < data[left]) else left
            minner = minner if data[minner] < data[index] else index
            if minner == index: break
            data[minner], data[index] = data[index], data[minner]
            # 继续找它的子节点最小值
            index = minner
            left = index * 2 + 1

    def topk(self, data, k):
        # 将前k个数建立最小堆
        for i in range(k):
            self.buil_heap(data, i)

        # 剩下的数据入堆
        for i in range(k, len(data)):
            # 比堆顶小的数，无需入堆
            if data[0] > data[i]:
                continue
            data[0] = data[i]
            self.heapify(data, 0, k)

        print(data[:k], data)

        index = k
        # 排序
        while index > 0:
            data[0], data[index - 1] = data[index - 1], data[0]
            self.heapify(data, 0, index - 1)
            index -= 1
        print(data[:k])


if __name__ == '__main__':
    data = [88, 43, 41, 67, 41, 55, 37, 69, 75, 99, 70, 14, 22, 89, 43, 28, 82, 85, 14, 78]
    k = 6
    tmp = sorted(data, reverse=True)
    print(tmp[:k])

    s = Solution()
    s.topk(data, k)
