
class Node():
    def __init__(self, value=None, _next=None):
        self.value = value
        self.next = _next

class SingleLink():
    def __init__(self, node=None):
        self.__node = node

    def empty(self):
        return self.__node is None

    def lenght(self):
        cur = self.__node
        count = 0

        while cur:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__node
        while cur:
            yield cur.value
            cur = cur.next
        
    def append(self, value):
        # 在链表尾部加 
        tmp = Node(value)

        if self.empty():
            self.__node = tmp
        else:
            cur = self.__node
            while cur.next:
                cur = cur.next
            cur.next = node


    def insert_head(self, value):
        # 在链表首部加
        # 创建节点 
        tmp = Node(value)
        # 将创建的节点next指向当前链表
        tmp.next = self.__node

        self.__node = tmp

    def insert(self, index, value):

        if index <= 0:
            self.insert_head(value)

        elif index > self.lenght() - 1:
            self.append(value)

        else:
            cur = self.__node
            count = 0
            # 找到index位置之前的节点
            while count < index - 1:
                count += 1
                cur = cur.next
            tmp = Node(value)
            tmp.next = cur.next
            cur.next = tmp

    def search(search, value):
        cur = self.__node
        while cur:
            if cur.value == value:
                return True
            else:
                cur = cur.next

        return False

    def remove(self, value):
        pre = None
        cur = self.__node
        while cur:
            if cur.value == value:
                if cur == self.__node:
                    self.__node = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next


if __name__ == '__main__':
    link1 = Node(1, Node(3, Node(5, Node(7, Node(10, Node(15))))))
    sl = SingleLink(link1)
    print(sl.lenght())
