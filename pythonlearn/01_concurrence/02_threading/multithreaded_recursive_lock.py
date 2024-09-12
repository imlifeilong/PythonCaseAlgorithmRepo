from threading import RLock
import threading
import time

"""
递归锁 RLock 内部维护了一个Lock和counter计数器，acquire时counter+1，release时counter-1
递归锁在一定程度上安全性比同步锁要低,所以一般在读的时候用递归锁，写的时候用同步锁，提升效率
"""


class RecursiveLock:
    def __init__(self):
        self.fork_lock = self.food_lock = RLock()
        # self.fork_lock = RLock()

    def eat_food_frist(self, food: RLock, fork: RLock):
        """
        先拿食物再拿叉子
        :param food:
        :param fork:
        :return:
        """
        name = threading.current_thread().name
        food.acquire()  # 加锁时 counter+1
        print(f'{name} 拿到食物')
        time.sleep(1)  # 当拿到food锁后，此时出现IO等待，线程切换
        fork.acquire()  # 再加锁时 counter+1

        print(f'{name} 拿到叉子')
        print(f'{name} 开始吃饭')
        fork.release()  # 释放时 counter-1
        food.release()  # 释放时 counter-1

    def eat_fork_frist(self, food: RLock, fork: RLock):
        """
        先拿叉子再拿食物
        :param food:
        :param fork:
        :return:
        """
        name = threading.current_thread().name
        fork.acquire()
        print(f'{name} 拿到叉子')
        time.sleep(1)  # 当拿到fork锁后，出现IO或者sleep时。线程会出现切换
        food.acquire()  # 当线程切换回来时，要申请food锁时，但是food已经被别的线程拿走了，需要等待food被释放后才能申请，此时会处于阻塞状态
        print(f'{name} 拿到食物')
        print(f'{name} 开始吃饭')
        food.release()
        fork.release()

    def main(self):
        t1 = threading.Thread(target=self.eat_food_frist, args=(self.food_lock, self.fork_lock), name='张飞')
        t1.start()

        t2 = threading.Thread(target=self.eat_fork_frist, args=(self.food_lock, self.fork_lock), name="关羽")
        t2.start()

        t1 = threading.Thread(target=self.eat_food_frist, args=(self.food_lock, self.fork_lock), name='刘备')
        t1.start()

        t2 = threading.Thread(target=self.eat_fork_frist, args=(self.food_lock, self.fork_lock), name="赵云")
        t2.start()


if __name__ == '__main__':
    dl = RecursiveLock()
    dl.main()
