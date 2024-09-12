import threading

"""
所谓守护 线程，是指在程序运行的时候在后台提供一种通用服务的线程，比如垃圾回收线程就是一个很称职的守护者
守护线程 在主线程生命周期内可以做一些事情，主线程一旦退出，守护线程也会被退出
"""


class DaemonThread:
    t = None

    def start(self):
        self.t = threading.Thread(target=self.monitor, name='守护线程007')
        self.t.setDaemon(True)  # 设置为守护线程
        self.t.start()

    def monitor(self):
        """
        守护线程
        :return:
        """
        for i in range(1000):
            print(f'守护线程：{threading.current_thread().name} {i} 监控中。。。')

    def main(self):
        self.start()
        for i in range(10):
            print(f'主线程：{i}')
        print(f'{self.t.name} {self.t.is_alive()}')  # 主线程没退的时候，守护线程也不会退


if __name__ == '__main__':
    dt = DaemonThread()
    dt.main()
