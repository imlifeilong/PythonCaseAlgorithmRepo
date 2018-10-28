# _*_ coding:UTF-8 _*_
#堆排序：大根堆要求每个节点的值都小于等于父节点的值，小根堆要求每个节点的值大于等于父节点的值
#父节点 list[i]  左节点 list[2i+1] 右节点 list[2i+2]
#大根堆 list[i] >= list[2i+1] && list[i] >= list[2i+2]
#小根堆 list[i] <= list[2i+1] && list[i] <= list[2i+2]
# def swap(res, des):
#     return des, res

# def create_max_heap(data):

#     for i in range(int(len(data)/2)-1, -1, -1):
#         min_heap(data, len(data), i)

# def min_heap(data, length, index):
#     '''
#     data: 堆列表
#     length: 长度
#     index: 需要调整的编号
#     '''
#     left = index * 2 + 1
#     right = index * 2 + 2
#     flag = 0 # 标记是否需要调整
#     least = 0
#     # print(' ', data[index])
#     # print()
#     # print(data[left], data[right])
#     # 和左儿子比较，并记录比较结果
#     if data[left] < data[index]:
#         least = left
#     else:
#         least = index
    
#     # 判断是否有右儿子
#     if right <= length:
#         # 和右儿子比较
#         if data[right] < data[least]:
#             least = right 
    
#     # 如果最小的节点号不是自己，交换
#     if least != index:
#         data[index], data[least] = data[least], data[index]
#         index = least

# def heap_sort(data):
#     create_max_heap(data)

#     for i in range(len(data)-1, 0, -1):
#         data[0], data[i] = data[i], data[0]
#         min_heap(data, i, 0)
    
#     return data

# if __name__ == '__main__':
#     data = [23,4,66,23,4,66,43,14,8,32,43,14,8]
#     heap_sort(data)
#     print(data)
#     # create_max_heap(data)



import random

def MAX_Heapify(heap, HeapSize, root):#在堆中做结构调整使得父节点的值大于子节点

    left = root * 2 + 1
    right = root * 2 + 2
    larger = root #先选择父节点作为最大点
    # print(heap[left], heap[right], heap[larger])
    if left < HeapSize and heap[larger] < heap[left]:
        # 和左节点比较如果左节点大于父节点，将左节点选为最大点
        larger = left
    if right < HeapSize and heap[larger] < heap[right]:
        larger = right
    if larger != root:
        #如果最大点不是父节点，这个时候做对调值操作
        heap[larger], heap[root] = heap[root], heap[larger]
        # 调换完了之后，要对
        MAX_Heapify(heap, HeapSize, larger)

def Build_MAX_Heap(heap):#构造一个堆，将堆中所有数据重新排序
    HeapSize = len(heap)
    for i in range((HeapSize-2)//2, -1, -1):
        # 从后往前获取有子节点的元素（n/2-1到0之间的元素有子节点）
        print(heap[i])
        MAX_Heapify(heap, HeapSize, i)

def HeapSort(heap):#将根节点取出与最后一位做对调，对前面len-1个节点继续进行对调整过程。
    Build_MAX_Heap(heap)
    for i in range(len(heap)-1,-1,-1):
        heap[0], heap[i] = heap[i], heap[0]
        MAX_Heapify(heap, i, 0)
    return heap

if __name__ == '__main__':
    a = [23,4,66,23,4,66,43,14,8,32,43,14,8]
    HeapSort(a)
    print(a)
    