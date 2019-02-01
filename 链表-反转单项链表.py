
class Node():
    def __init__(self, value=None, _next=None):
        self.value = value
        self.next = _next

class DNode():
    def __init__(self, value, _pre=None, _next=None):
        self.value = value
        self.pre = _pre
        self.next = _next


class ReverseLink():
    def _single(self, link):
        if not link:
            return

        pre = None
        while link:
            # 将当前节点下一个节点(Node(8))保存在_next中
            _next = link.next
            # 把当前节点的下个节点指向 上个节点(None)
            link.next = pre
            # 记录当前节点(Node(5))
            pre = link
            # 然后走到下个节点(Node(8))
            link = _next
        return pre

    def _double(self, link):
        if link == None:
            return
        pre = None
        while link != None:
            _next = link.next
            link.next = pre
            link.pre = _next
            pre = link
            link = _next
        return pre

    def _print(self, link):
        while link:
            print(link.value)
            link = link.next
if __name__ == '__main__':
    link1 = Node(5, Node(8, Node(10, Node(11, Node(12, Node(15))))))
    # 5 -> 8 -> 10 -> 11 -> 12 -> 15 -> None
    # _next ==> 8          5 -> None            
    # pre ==> 5 -> None
    # link ==> _next ==> 8 
    # _next ==> 10         8 -> pre ==> 5     8 -> 5 -> None
    # pre ==> 8
    # link ==> _next ==> 10
    link2 = DNode(3, DNode(2), DNode(4, DNode(5)))

    rl = ReverseLink()
    # res = rl._single(link1)
    res = rl._double(link2)
