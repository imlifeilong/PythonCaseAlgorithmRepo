#coding: utf-8
'''
实现一个特殊的栈，在实现栈的基本功能的基础上，再实现返回栈中最小元素的操作。
【要求】
1．pop、push、getMin操作的时间复杂度都是O(1)。
2．设计的栈类型可以使用现成的栈结构。
'''

class Stack():
    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min = 0

    def pop(self):
        if len(self.stack) <= 0:
            raise 'stack is empty'

        value = self.stack.pop()
        self.min_stack.pop()

        return value

    def push(self, num):
        if len(self.stack) == 0:
            self.min = num
        self.stack.append(num)
        if num < self.min:
            self.min = num
        self.min_stack.append(self.min)


    def get_min(self):
        if len(self.min_stack) == 0:
            raise 'stack is empty'
        return self.min_stack[-1]

from queue import Queue

class LifoQueue(Queue):
    def _init(self, maxsize):
        self.queue = []

    def _qsize(self):
        return len(self.queue)

    def _put(self, item):
        self.queue.append(item)

    def _get(self):
        return self.queue.pop()
# class MinStack():
#     def __init__(self):
#         self.__s = LifoQueue()
#         self.__ms = LifoQueue()

#     def push(self, num):
#         self.__s.put(num)

if __name__ == '__main__':
    # s = Stack()
    # s.push(3)
    # s.push(2)
    # s.push(1)
    # s.push(9)
    # s.push(4)

    # print(s.get_min())
    # s.pop()
    # s.pop()
    # s.pop()
    # print(s.get_min())
    q = LifoQueue()
    q.put(1)
    print(q.get())
