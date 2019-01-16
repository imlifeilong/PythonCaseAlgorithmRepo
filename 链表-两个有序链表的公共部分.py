'''
链表：每个节点都包含数据和下一数据的地址，即信息域和指针域
'''
class Node():
    def __init__(self, value=None, _next=None):
        self.value = value
        self.next = _next


class LinkCommonPart():
    def _print(self, link1, link2):
        # 有一个链表为空就停止打印
        if not link1 or not link2:
            return

        while link1 and link2:
            # 如果链表1值大于链表2，链表2到下一个值
            if link1.value > link2.value:
                link2 = link2.next
            # 相反如果链表2大于链表1，链表1到先一个值
            elif link1.value < link2.value:
                link1 = link1.next
            # 相同则打印，两个链表同时来到下一个值
            else:
                print(link1.value)
                link1 = link1.next
                link2 = link2.next

if __name__ == '__main__':
    # 两个有序链表
    link1 = Node(1, Node(3, Node(5, Node(7, Node(10, Node(15))))))
    link2 = Node(5, Node(8, Node(10, Node(11, Node(12, Node(15))))))
    lcp = LinkCommonPart()
    lcp._print(link1, link2)