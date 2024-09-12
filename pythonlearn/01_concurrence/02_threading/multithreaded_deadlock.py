from threading import Lock
import threading
import time
"""
死锁：是指两个或两个以上的进程或线程在执行过程中，因争夺资源而造成的一种互相等待的现象，
若无外力作用，它们都将无法推进下去。此时称系统处于死锁状态或系统产生了死锁，这些永远在互相等待的进程称为死锁进程

吃饭时必须拿到食物和叉子才能开始吃，
当前右张飞和关羽两个线程，张飞先拿到食物，准备拿叉子的时候，出现IO。
切换到关羽先拿到叉子，再准备拿食物的时候发现食物已经被张飞拿走，所以需要等待张飞释放了食物后，才能拿到食物，出现阻塞，
切换到张飞，张飞此时想要申请叉子时，发现叉子已经被关羽拿走，必须等待关羽释放叉子，才能继续，此时就出现死锁。
张飞处于阻塞状态，要等关羽释放叉子后才能继续，关羽此时也处于阻塞状态，要等张飞释放食物才能继续。
"""


class DeadLock:
    def __init__(self):
        self.fork_lock = self.food_lock = Lock()
        # self.fork_lock = Lock()

    def eat_food_frist(self, food: Lock, fork: Lock):
        """
        先拿食物再拿叉子
        :param food:
        :param fork:
        :return:
        """
        name = threading.current_thread().name
        food.acquire()
        print(f'{name} 拿到食物')
        time.sleep(1)   # 当拿到food锁后，此时出现IO等待，线程切换
        fork.acquire()  # 当线程切换回来时，要申请fork锁时，但是fork已经被别的线程拿走了，需要等待fork被释放后才能申请，此时会处于阻塞状态
        print(f'{name} 拿到叉子')
        print(f'{name} 开始吃饭')
        fork.release()
        food.release()

    def eat_fork_frist(self, food: Lock, fork: Lock):
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

        # t1 = threading.Thread(target=self.eat_food_frist, args=(self.food_lock, self.fork_lock), name='刘备')
        # t1.start()
        #
        # t2 = threading.Thread(target=self.eat_fork_frist, args=(self.food_lock, self.fork_lock), name="赵云")
        # t2.start()


if __name__ == '__main__':
    dl = DeadLock()
    dl.main()
