import os
import time
import queue
from threading import Thread, Lock, RLock, Condition, Timer
from concurrent.futures import ThreadPoolExecutor
import threading

def f1(i):
    time.sleep(0.8)
    print('线程', i, os.getpid(), threading.current_thread(), threading.get_ident())
    print(i+i)


def f2():
    while True:
        print('*' * 10)
        time.sleep(1)

def f3():
    print('in f2')
    time.sleep(3)

def f4(lock):
    global n
    lock.acquire()
    tmp = n
    time.sleep(0.1)
    n = tmp -1
    lock.release()


def eat1(name, noodle_lock, fork_lock):
    noodle_lock.acquire()
    print('%s拿到面条啦'%name)
    fork_lock.acquire()
    print('%s拿到叉子了'%name)
    print('%s吃面'%name)
    fork_lock.release()
    noodle_lock.release()

def eat2(name, noodle_lock, fork_lock):
    fork_lock.acquire()
    print('%s拿到叉子了'%name)
    time.sleep(1)
    noodle_lock.acquire()
    print('%s拿到面条啦'%name)
    print('%s吃面'%name)
    noodle_lock.release()
    fork_lock.release()

def f5(con, i):
    con.acquire()
    con.wait()
    print('拿到钥匙', i)
    con.release()

def f6():
    print('*************')

def f7(n):
    time.sleep(2)
    print('nnnn', n)
    return n+n

def f8(m):
    print('回调结果', m.result())

if __name__=='__main__':
    # 互斥锁 ################################
    n = 10
    lock = Lock()
    t_list = []
    for i in range(10):
        t = Thread(target=f4, args=(lock, ))
        t.start()
        t_list.append(t)

    for t in t_list:t.join()
    print(n)
    # 吃面 出现死锁 ###########################
    # noodle_lock  = Lock()
    # fork_lock = Lock()
    # Thread(target=eat1,args=('alex', noodle_lock, fork_lock)).start()
    # Thread(target=eat2,args=('Egon', noodle_lock, fork_lock)).start()
    # Thread(target=eat1,args=('bossjin', noodle_lock, fork_lock)).start()
    # Thread(target=eat2,args=('nezha', noodle_lock, fork_lock)).start()
    # 吃面 递归锁 #############################
    # fork_lock = noodle_lock  = RLock() # 递归锁 一个钥匙串的两把钥匙
    # Thread(target=eat1,args=('alex', noodle_lock, fork_lock)).start()
    # Thread(target=eat2,args=('Egon', noodle_lock, fork_lock)).start()
    # Thread(target=eat1,args=('bossjin', noodle_lock, fork_lock)).start()
    # Thread(target=eat2,args=('nezha', noodle_lock, fork_lock)).start()
    # 条件 ####################################
    # con = Condition()
    # # 共有17个线程准备执行任务，要领导钥匙才能继续
    # for i in range(17):
    #     Thread(target=f5, args=(con, i)).start()

    # for x in [5, 1, 2, 3, 4, 2]:
    #     time.sleep(1)
    #     con.acquire()
    #     print('开始制作%s把钥匙'%x)
    #     con.notify(x)    # 发送条件，让x个线程拿到钥匙，状态变为True，线程才能执行
    #     con.release()
    # 定时器 #################################
    # while True:
    #     t = Timer(3, f6).start() # 等待3秒开启，非阻塞
    #     time.sleep(3)

    # 队列 ##################################
    # q = queue.Queue() # 队列
    # lq = queue.LifoQueue() # 栈
    # pq = queue.PriorityQueue() # 优先级队列，根据优先级出队
    # pq.put((20, 'a'))
    # pq.put((-1, 'b'))
    # pq.put((2, 'r'))
    # pq.put((30, 'x'))
    # pq.put((0, 't'))
    # pq.put((20, 'z'))
    # print(pq.get())
    # 线程池 ##################################
    pool = ThreadPoolExecutor(5)
    # for i in range(20):
    #     pool.submit(f7, i).add_done_callback(f8) # 回调函数
    # pool.map(f7, range(10))
    t_list = []
    for i in range(20):
        t = pool.submit(f7, i)
        t_list.append(t)

    pool.shutdown() # 相当于 close+join 等线程全部执行完了，再返回结果
    print('主线程')
    for t in t_list:print(t.result())