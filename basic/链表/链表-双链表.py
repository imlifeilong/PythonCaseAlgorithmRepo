
class Node():
    def __init__(self, value=None, _next=None, prev=None):
        self.value = value
        self.next = _next
        self.prev = prev

class DoubleLinkList():
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
            # 将尾节点cur的next指向新节点tmp
            cur.next = tmp
            # 将新节点tmp的prev指向cur
            tmp.prev = cur

    def insert_head(self, value):
        # 在链表首部加
        # 创建节点 
        tmp = Node(value)
        cur = self.__node
        # 将创建的节点next指向cur
        tmp.next = cur

        # 将当前节点prev指向 tmp
        cur.prev = tmp

        # 将当前节点指向 新节点tmp
        self.__node = tmp

    def insert(self, index, value):

        if index <= 0:
            self.insert_head(value)

        elif index > self.lenght() - 1:
            self.append(value)

        else:
            # 创建新节点
            tmp = Node(value)
            cur = self.__node
            count = 0
            # 找到index位置之前的节点，置为当前节点
            while count < index - 1:
                count += 1
                cur = cur.next
            
            # 将tmp的prev指向cur
            tmp.prev = cur

            # 将tmp的next指向cur的next
            tmp.next = cur.next

            # 将cur的下个节点的prev指向tmp
            cur.next.prev = tmp

            # 将cur的next指向tmp
            cur.next = tmp


    def search(self, value):
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
            # 找到要删除的节点 
            if cur.value == value:
                # 如果刚好是头节点，就指向下个节点 
                if cur == self.__node:
                    self.__node = cur.next
                    # 判断链表是否只有一个节点，则他的next.prev不存在
                    if cur.next:
                        cur.next.prev = None
                # 如果不是头节点，则前一个节点直接指向当前节点的下个节点
                else:
                    pre.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                return True
            # 先保存当前节点为 前一个节点，将当前节点指向下个节点
            else:
                pre = cur
                cur = cur.next
        return False


if __name__ == '__main__':
    dl = DoubleLinkList()
    for i in [1, 2, 3, 4, 5, 6,]:
        dl.append(i)
    # dl.insert_head(0)
    # dl.insert_head(100)
    # dl.insert_head(123)
    dl.insert(1, 300)
    for x in dl.travel():
        print(x)

    dl.remove(5)
    print('******************')
    dl.insert(5, 500)
    for x in dl.travel():
        print(x)
    # print(sl.lenght())
    # # sl.append(22)
    # # sl.insert_head(0)
    # print(sl.search(5))
    # # sl.remove(5)
    # print(sl.remove(15))
    # sl.insert(5, '***********************')
    # for x in sl.travel():
    #     print(x)
