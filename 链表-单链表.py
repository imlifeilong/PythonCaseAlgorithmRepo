
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
            cur.next = tmp


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
            # 找到index位置之前的节点，置为当前节点
            while count < index - 1:
                count += 1
                cur = cur.next
            # 创建新节点 
            tmp = Node(value)
            # 将该节点next节点指向 当前节点的next节点
            tmp.next = cur.next
            # 将当前节点的 next指向新节点
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
                # 如果不是头节点，则前一个节点直接指向当前节点的下个节点
                else:
                    pre.next = cur.next
                return True
            # 先保存当前节点为 前一个节点，将当前节点指向下个节点
            else:
                pre = cur
                cur = cur.next
        return False


if __name__ == '__main__':
    link1 = Node(1, Node(3, Node(5, Node(7, Node(10, Node(15))))))
    sl = SingleLink(link1)
    print(sl.lenght())
    # sl.append(22)
    # sl.insert_head(0)
    print(sl.search(5))
    # sl.remove(5)
    print(sl.remove(15))
    sl.insert(5, '***********************')
    for x in sl.travel():
        print(x)
