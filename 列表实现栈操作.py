# -*- coding: utf-8 -*-

class EmptyStackError(BaseException):
    r'EmptyStackError'

class StackOverflowError(BaseException):
    r'StackOverflowError'

class StackSizeError(BaseException):
    r'StackSizeError'


class Stack():
    def __init__(self, size):
        self.size = size
        if self.size <= 0:
            raise StackSizeError
        self.data = [None] * self.size
        self.top = 0
    
    def push(self, num):
        if self.top == self.size:
            raise StackOverflowError
        self.data[self.top] = num
        self.top += 1

    def pop(self):
        if self.top == 0:
            raise EmptyStackError
        res = self.data[self.top-1]
        self.top -= 1
        return res

    def peek(self):
        if self.top == 0:
            return
        return self.data[self.top-1]


if __name__ == '__main__':
    s = Stack(3)
    s.push(1)
    # s.push(11)
    # s.push(12)

    print(s.data)
    # s.pop()
    # s.pop()
    # s.pop()

    print(s.data)
    print(s.peek())