# _*_ coding:UTF-8 _*_
#堆排序：大根堆要求每个节点的值都小于等于父节点的值，小根堆要求每个节点的值大于等于父节点的值
#父节点 list[i]  左节点 list[2i+1] 右节点 list[2i+2]
#大根堆 list[i] >= list[2i+1] && list[i] >= list[2i+2]
#小根堆 list[i] <= list[2i+1] && list[i] <= list[2i+2]
'''
在堆的数据结构中，堆中的最大值总是位于根节点（在优先队列中使用堆的话堆中的最小值位于根节点）。堆中定义以下几种操作：

最大堆调整（Max Heapify）：将堆的末端子节点作调整，使得子节点永远小于父节点
创建最大堆（Build Max Heap）：将堆中的所有数据重新排序
堆排序（HeapSort）：移除位在第一个数据的根节点，并做最大堆调整的递归运算

'''


# 将数据插入到已经建好的堆中
def heap_insert(data, index):
    # 如果当前数据比他的父节点大，则交换，再继续往上，与他的父节点比较
    root = (index - 1) // 2
    while data[index] > data[root]:
        data[index], data[root] = data[root], data[index]
        index = root

# 大根堆中一个数变小后，往下沉
def heapify(data, index, length):
    left = index * 2 + 1
    while left < length:
        right = left + 1
        # 比较当前节点的左右子节点，找到最大的那个下标
        larger = right if (right < length and data[right] > data[left]) else left
        # 比较当前节点和子节点中最大的那个，找到大的那个的下标
        larger = larger if data[larger] > data[index] else index
        # 如果当前节点和最大的那个节点数相同，则不需要做任何操作
        if larger == index: break
        # 当前节点和左右节点的最大的那个交换
        data[larger], data[index] = data[index], data[larger]
        # 当前节点指向最大那个节点，再继续判断
        index = larger
        left = index * 2 + 1

def heapsort(data):
    size = len(data) - 1
    if not data or size < 2:
        return data
    # 创建大根堆
    for i in range(size):
        heap_insert(data, i)
    # 将堆中最后一个与堆顶交换，堆的长度减小一位
    data[0], data[size] = data[size], data[0]
    size -= 1
    
    # 然后再调整堆为大根堆
    while size > 0:
        heapify(data, 0, size)
        data[0], data[size] = data[size], data[0]
        size -= 1
    return data

if __name__ == '__main__':
    a = [23,4,66,23,4,66,43,14,8,32,43,14,8]
    res = heapsort(a)
    print(a)
    