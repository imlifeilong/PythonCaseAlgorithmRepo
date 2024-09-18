import asyncio
from multiprocessing import Process, Pool
from concurrent.futures import ProcessPoolExecutor
from functools import partial
import tasks
import utils

cpu_task = tasks.cpu_task


class Tutorial01:
    @utils.runtime
    def main(self):
        # 使用子进程调度CPU密集型任务
        p1 = Process(target=cpu_task, args=(100000000,))
        p2 = Process(target=cpu_task, args=(200000000,))
        # 开始执行子进程
        p1.start()
        p2.start()
        # 阻塞等待子进程执行完成
        p1.join()
        p2.join()


class Tutorial02:
    @utils.runtime
    def main(self):
        """
        使用进程池 apply方法获取返回结果， 会阻塞调用
        :return:
        """
        with Pool() as pool:
            p1 = pool.apply(cpu_task, args=(100000000,))
            p2 = pool.apply(cpu_task, args=(200000000,))
            print(p1)
            print(p2)


class Tutorial03:
    @utils.runtime
    def main(self):
        """
        使用进程池 apply_async方法 异步调用不阻塞，获取返回结果
        :return:
        """
        with Pool() as pool:
            p1 = pool.apply_async(cpu_task, args=(100000000,))
            p2 = pool.apply_async(cpu_task, args=(200000000,))
            print(p1.get())
            print(p2.get())


class Tutorial04:
    @utils.runtime
    def main(self):
        """
        使用ProcessPoolExecutor进程池 map方法 按顺序获取结果
        :return:
        """
        with ProcessPoolExecutor() as pool:
            totals = [100000000, 100000000, 100000000, 20, 100000000, 500000, 100000000, 200000000]
            for res in pool.map(cpu_task, totals):
                print(res)


class Tutorial05:

    @utils.aruntime
    async def amain(self):
        with ProcessPoolExecutor() as pool:
            loop = asyncio.get_running_loop()
            totals = [100000000, 100000000, 100000000, 20, 100000000, 500000, 100000000, 200000000]
            # partial 偏函数将cpu_task的参数传递进去，返回一个可调用的对象
            callables = [partial(cpu_task, n) for n in totals]
            task_list = []
            for c in callables:
                task_list.append(loop.run_in_executor(pool, c))
            results = await asyncio.gather(*task_list)
            for r in results:
                print(r)

    @utils.runtime
    def main(self):
        """
        使用异步+ProcessPoolExecutor进程池
        :return:
        """
        asyncio.run(self.amain())


if __name__ == '__main__':
    # t1 = Tutorial01()
    # t1.main()

    # t2 = Tutorial02()
    # t2.main()

    # t3 = Tutorial03()
    # t3.main()

    t4 = Tutorial04()
    t4.main()

    t5 = Tutorial05()
    t5.main()
