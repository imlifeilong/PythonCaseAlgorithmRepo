'''
    有一个宾馆，只有m个房间（room），有房客（A~Z）到来时，若有空房间则可以立即入住；
    没有空房间则不能入住，旅客可以选择立即离开或者等待空房间；
    假设给定了各个旅客到达和离开的顺序（如HFBJJBKFHMMSSLPWWPLK），问有多少个旅客没能入住。
'''
def room_full():
    count = 2
    string = 'ABCDCBAJJKZKZ'
    room = set()
    index = 0
    for i in string:
        # 没满
        if len(room) < count:
            if i not in room:
                room.add(i)
            else:
                room.remove(i)
        # 满了
        elif len(room) == count:
            if i in room:
                room.remove(i)
            else:
                print('-------', i)
                index += 1
    print(index)

room_full()