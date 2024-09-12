from threading import Lock
import threading
import time
import random


class ThreadSafe:
    def __init__(self):
        self.count = 0
        self.lock = Lock()

    def click_rate_with_lock1(self):
        """
        加锁
        :return:
        """
        with self.lock:
            self.click_rate()

    def click_rate_with_lock2(self):
        """
        加锁
        :return:
        """
        # 加锁
        self.lock.acquire()
        self.click_rate()
        # 释放锁
        self.lock.release()

    def click_rate(self):
        """
        非原子操作，线程遇到IO或sleep会切换
        :return:
        """
        maxcount = 1000000
        for i in range(maxcount):
            self.count += 1  # 执行完后可能会切换线程
        print(threading.current_thread().name, self.count)

        time.sleep(random.random())
        for i in range(maxcount):
            self.count -= 1
        print(threading.current_thread().name, self.count)

    def click_rate1(self):
        with self.lock:
            for i in range(5000000):
                self.count += 1

    def click_rate2(self):
        with self.lock:
            for i in range(5000000):
                self.count += 1

    def main_without_lock(self):
        """
        线程不安全
        :return:
        """
        jobs = set()
        for i in range(2):
            t1 = threading.Thread(target=self.click_rate)
            t1.start()
            jobs.add(t1)
        for t in jobs:
            t.join()
        print(self.count)

    def main1(self):
        """
        加锁，线程安全
        :return:
        """
        jobset = set()
        for i in range(20):
            t = threading.Thread(target=self.click_rate_with_lock1)
            t.start()
            jobset.add(t)

        for t in jobset:
            t.join()

    def main(self):

        t1 = threading.Thread(target=self.click_rate1)
        t1.start()
        t2 = threading.Thread(target=self.click_rate2)
        t2.start()
        t1.join()
        t2.join()
        print(self.count)


if __name__ == '__main__':
    ts = ThreadSafe()
    # ts.main()
    ts.main_without_lock()
