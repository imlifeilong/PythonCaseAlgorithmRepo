'''

数据结构中的堆
可以看做是一颗完全的二叉树结构，最后一层的子节点，都在最左边
大根堆 就是所有子节点必须小于等于根节点，用于顺序排序
小根堆 就是所有子节点必须大于等于根节点，用于逆序排序
(01) 索引为i的左孩子的索引是 (2*i+1);
(02) 索引为i的左孩子的索引是 (2*i+2);
(03) 索引为i的父结点的索引是 floor((i-1)/2);

在堆的数据结构中，堆中的最大值总是位于根节点（在优先队列中使用堆的话堆中的最小值位于根节点）。堆中定义以下几种操作：

最大堆调整（Max Heapify）：将堆的末端子节点作调整，使得子节点永远小于父节点
创建最大堆（Build Max Heap）：将堆中的所有数据重新排序
堆排序（HeapSort）：移除位在第一个数据的根节点，并做最大堆调整的递归运算



'''


# 将序列中索引为index的数据插入到已经建好的堆中
def heap_insert(data, index):
    # 根据index计算出当前节点的 父节点
    root = int((index - 1) / 2)

    while data[index] > data[root]:
        # 然后比较当前节点是否大于父节点root，如果比root大，就和root交换
        data[index], data[root] = data[root], data[index]

        # 交换后，再计算它的父节点，然后继续进行比较，直到不大于它的父节点，或者到达根节点(index=root=0的时候)
        index = root
        root = int((index - 1) / 2)


# 大根堆中一个数变小后，往下沉
def heapify(data, index, length):
    # 调整index（一般是0，因为堆排序中，会将最末尾的位置放置堆顶，
    # 然后进行调整，直到找到合适的位置停止）所指元素的位置，再[0, length)区间上

    # 调整过程是 从堆顶位置开始，找到左右子节点中比较大的值，如果比堆顶元素大，就和堆顶交换，
    # 交换后，再继续找此时的，左右子节点中较大的 再进行比较，然后再替换，
    # 直到所处位置的左右子节点的值都小于等于当前节点，或者到达的末尾的位置，再停止
    left = index * 2 + 1
    while left < length:
        right = left + 1
        # 比较当前节点的左右子节点，找到最大的那个下标
        larger = right if (right < length and data[right] > data[left]) else left
        # 比较当前节点和子节点中最大的那个，找到大的那个的下标
        larger = larger if data[larger] > data[index] else index

        # 如果当前节点和最大的那个节点数相同，则不需要做任何操作
        if larger == index:
            break
        # 当前节点和左右节点的最大的那个交换
        data[larger], data[index] = data[index], data[larger]

        # 当前节点指向最大那个节点，再继续判断
        index = larger
        left = index * 2 + 1


def heapsort(data):
    size = len(data)
    if not data or size < 2:
        return data
    # 创建大根堆
    for i in range(size):
        heap_insert(data, i)
    # 堆创建完成后，因为是大根堆，所以堆顶的元素是序列中最大的元素

    right = len(data) - 1  # 此时堆最末尾的索引
    # 然后再调整堆为大根堆
    while right > 0:
        # 将堆顶的元素，弹出（放到堆末尾，最末尾的叶子节点）
        # 将末尾的元素放到堆顶，进行调整
        data[0], data[right] = data[right], data[0]
        heapify(data, 0, right)
        # 缩小末尾位置，继续进行 交换和调整，直到所有的元素都交换并且调整过
        right -= 1
    return data


def random_data():
    import random
    res = []
    for i in range(random.randint(1, 100)):
        res.append(random.randint(1, 100))
    return res


def compare(src, res):
    data = sorted(src)
    if len(data) == len(src):
        for i in range(len(data)):
            if data[i] != res[i]:
                return False
        return True


if __name__ == '__main__':
    # for i in range(10000):
    #     src = random_data()
    #     if not compare(src, heapsort(src)):
    #         print(src)
    alist = [3, 1, 5, 2, 8, 5, 9, 3, 5, 1, 2, 3]
    res = heapsort(alist)
    print(res)
