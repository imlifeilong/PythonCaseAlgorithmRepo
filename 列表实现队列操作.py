# -*- coding: utf-8 -*-

class EmptyQueueError(BaseException):
    r'EmptyQueueError'

class QueueOverflowError(BaseException):
    r'QueueOverflowError'

class QueueSizeError(BaseException):
    r'QueueSizeError'


class Queue():
    def __init__(self, size):
        self.size = size
        if self.size <= 0:
            raise QueueSizeError
        self.start = 0
        self.end = 0
        self.index = 0
        self.data = [None] * self.size
        self.length = self.size - 1
    
    def push(self, num):
        if self.index == self.size:
            raise QueueOverflowError

        self.data[self.end] = num
        self.index += 1

        if self.end == self.length:
            self.end = 0
        else:
            self.end += 1


    def pop(self):
        if self.index == 0:
            raise EmptyQueueError

        self.index -= 1
        index = self.data[self.start]
        self.data[self.start] = None
        if self.start == self.length:
            self.start = 0
        else:
            self.start += 1
        return index

if __name__ == '__main__':
    s = Queue(3)
    s.push(1)
    s.push(11)
    s.push(12)
    print(s.pop())
    s.push(3)
    print(s.pop())
    s.push(4)
    print(s.pop())
    s.push(23)
    print(s.pop())
    print(s.pop())
    print(s.pop())