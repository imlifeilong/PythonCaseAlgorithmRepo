'''
    某个打印机根据打印队列执行打印任务。打印任务分为九个优先级，分别采用数字1~9表示，
    数字越大优先级越高。打印机每次从队列头部取出第一个任务A，然后检查队列余下任务中
    有没有比A优先级更高的任务，如果有比A优先级高的任务，则将任务A放到队列尾部，
    否则执行任务A的打印
'''

from queue import Queue
import sys
def order_print():
    # string = sys.stdin.readlines()
    string = '1,3,4,9,1,4'
    string = '1,9,2,1'
    string = '9,3,5'
    q = Queue()
    string_list = [int(i) for i in string.split(',')]
    # 将元素入队
    for i in string_list:
        q.put(i)

    # 打印顺序
    index = 0
    while q.qsize() > 0:
        max_flag = False
        cur = q.get()

        # 判断队列中是否有比头节点大的值
        for j in range(q.qsize()):
            font = q.get()
            if cur < font:
                max_flag = True
            q.put(font)
        
        if max_flag:
            # 存在比头节点大的值，将头节点放入队尾
            q.put(cur)
        else:
            # 不存在，打印
            print(index, cur)
            index += 1


if __name__ == '__main__':
    order_print()