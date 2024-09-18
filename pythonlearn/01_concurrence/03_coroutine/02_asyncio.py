import asyncio
import typing
import time
import functools
import tasks
import utils

get = tasks.get
post = tasks.post
long_running_task = tasks.long_running_task
block_task = tasks.block_task
callback = tasks.callback
acpu_task = tasks.acpu_task


# 使用asyncio.run运行协程
class Tutorial01:
    def main(self):
        """
        使用asyncio.run运行协程，会创建一个新的事件循环并在结束时关闭
        """
        asyncio.run(get("baidu", 1))


# 使用底层的事件循环执行协程
class Tutorial02:
    async def get_loop(self):
        # 获取已经存在的loop每个线程只有一个loop
        loop = asyncio.get_running_loop()
        print("当前线程中运行的loop", id(loop))

    def main(self):
        # 获取当前事件循环，如果当前 OS 线程没有设置当前事件循环，
        # 该 OS 线程为主线程，并且 set_event_loop() 还没有被调用，
        # 则 asyncio 将创建一个新的事件循环并将其设为当前事件循环
        loop = asyncio.get_event_loop()
        print("新建的loop", id(loop))
        loop.run_until_complete(self.get_loop())
        loop.run_until_complete(get("baidu", 1))


# 使用asyncio.gather 执行多个协程
class Tutorial03:
    async def amain(self):
        """
        asyncio.gather 执行多个协程，它按调用顺序返回的是所有任务的结果列表
        :return:
        """
        result = await asyncio.gather(get("baidu", 1), post("kuaishou", 2))
        for r in result:
            print("协程执行结果", r)

    def main(self):
        """
        使用asyncio.run运行协程，会创建一个新的事件循环并在结束时关闭
        """
        asyncio.run(self.amain())


# asyncio.wait 执行多个协程
class Tutorial04:
    async def amain(self):
        """
        asyncio.wait 等待所以协程完成，返回两个集合：已完成的任务（done）和未完成的任务（pending）
        :return:
        """
        coros = [get("douyin", 3), post("douban", 2), get("baidu", 1)]
        done, pending = await asyncio.wait(coros)
        for r in done:
            print("协程执行结果", r.result())

    def main(self):
        """
        使用asyncio.run运行协程，会创建一个新的事件循环并在结束时关闭
        """
        asyncio.run(self.amain())


# asyncio.create_task 执行多个协程
class Tutorial05:
    async def amain(self):
        """
        asyncio.create_task 在后台并发运行多个协程
        任务会立即开始执行，且不需要立刻等待它完成。
        如果想要返回结果，需要使用 await 获取结果，类似多线程中的join
        :return:
        """

        # 为什么需要 asyncio.create_task？
        # 下面3个协程执行的时候是按顺序串行执行的，没有起到并发的作用
        await get("douyin", 3)
        await post("douban", 2)
        await get("baidu", 1)

        # 但是使用asyncio.create_task创建Task对象后，就是并发
        task1 = asyncio.create_task(get("douyin", 3))
        task2 = asyncio.create_task(post("douban", 2))
        task3 = asyncio.create_task(get("baidu", 1))

        # result1 = await task1
        # result2 = await task2
        # result3 = await task3
        # print("协程执行结果", result1)
        # print("协程执行结果", result2)
        # print("协程执行结果", result3)

    def main(self):
        """
        使用asyncio.run运行协程，会创建一个新的事件循环并在结束时关闭
        """
        asyncio.run(self.amain())


# asyncio.as_completed 执行多个协程
class Tutorial06:
    async def amain(self):
        """
        asyncio.as_completed 会生成一个协程迭代器，每当有协程完成时，迭代器会返回该协程的结果
        谁先结束就返回谁，不是按顺序
        :return:
        """
        coros = [get("douyin", 3), post("douban", 2), get("baidu", 1)]
        # 使用 asyncio.as_completed 获取完成的任务结果
        for completed_task in asyncio.as_completed(coros):
            result = await completed_task
            print("协程执行结果", result)

    def main(self):
        """
        使用asyncio.run运行协程，会创建一个新的事件循环并在结束时关闭
        """
        asyncio.run(self.amain())


# 可等待对象 如果一个对象可以在 await 语句中使用，那么它就是 可等待 对象
# 可等待 对象有三种主要类型: 协程, 任务 和 Future.

# asyncio.as_completed 执行多个协程
class Tutorial07:

    async def get_response(self, future: asyncio.Future):
        print("start set result")
        await asyncio.sleep(2)
        future.set_result("future result done")
        print("over set result")

    async def amain(self):
        # 等待协程
        result = await get("douyin", 3)
        print("协程等待结果：", result)
        # 等待Task
        task = asyncio.create_task(post("douban", 2))
        result = await task
        print("Task等待结果：", result)

        future = asyncio.Future()
        # 创建一个任务来执行耗时的异步任务
        task = asyncio.create_task(self.get_response(future))

        # 等待Future对象完成
        result = await future
        print("Future对象等待结果：", result)

    def main(self):
        """
        使用asyncio.run运行协程，会创建一个新的事件循环并在结束时关闭
        """
        asyncio.run(self.amain())


class Tutorial08:
    """
    任务超时
    """

    async def amain(self):
        try:
            # 使用wait_for为long_running_task设置3秒的超时时间
            result = await asyncio.wait_for(long_running_task(), timeout=3)
            print(f'得到结果: {result}')
        except asyncio.TimeoutError:
            print('任务超时')

        # 运行事件循环

    def main(self):
        asyncio.run(self.amain())


class Tutorial09:
    """
    任务取消
    """

    async def amain(self):
        long_task = asyncio.create_task(long_running_task())
        times = 0

        # 检测任务是否完成
        while not long_task.done():
            print(f"long task is running {times}.")
            await asyncio.sleep(1)
            times += 1
            if times == 4:
                # 取消任务
                long_task.cancel()

        try:
            await long_task
        except asyncio.CancelledError:
            print('任务取消')

        # 运行事件循环

    def main(self):
        asyncio.run(self.amain())


class Tutorial10:
    """
    任务取消
    """

    async def amain(self):
        long_task = asyncio.create_task(long_running_task())
        shielded_task = asyncio.shield(long_task)

        # await asyncio.wait_for(shielded_task, timeout=3)

        times = 0
        # 检测任务是否完成
        while not shielded_task.done():
            print(f"long task is running {times}.")
            await asyncio.sleep(1)
            times += 1
            if times == 3:
                # 取消任务
                print("尝试取消任务")
                shielded_task.cancel()

        try:
            await long_task
        except asyncio.CancelledError:
            print('任务取消成功')

    def main(self):
        asyncio.run(self.amain())


class Tutorial11:

    async def amain(self):
        loop = asyncio.get_running_loop()
        """
        允许你在事件循环中运行阻塞的、同步的代码。它将同步的操作放入线程池或进程池中执行，以避免阻塞主事件循环，从而实现异步执行
        loop.run_in_executor(executor, func, *args)
        executor：可以是 None，表示使用默认的线程池，也可以是自定义的 ThreadPoolExecutor 或 ProcessPoolExecutor
        func：要运行的同步函数
        *args：传递给函数的参数
        """

        result = loop.run_in_executor(None, block_task, 'baidu')

        task = asyncio.create_task(get('baidu', 1))

        print("阻塞函数结果", await result)

    def main(self):
        asyncio.run(self.amain())


class Tutorial12:
    """
    回调
    """

    async def amain(self):
        loop = asyncio.get_running_loop()
        # 立即执行回调
        loop.call_soon(callback, 'call_soon')
        # 3秒之后执行回调
        loop.call_later(3, callback, 'call_later')

        # 当前事件循环的时间
        now = loop.time()
        # 一个 特定时间点 执行某个任务, 在 5 秒后的特定时间调用回调
        loop.call_at(now + 5, callback, 'call_at')

        print("main loop")
        await asyncio.sleep(7)

    def main(self):
        asyncio.run(self.amain())


class Tutorial13:
    """
    CPU密集型任务，会阻塞
    """

    @utils.aruntime
    async def io_main(self):
        task1 = asyncio.create_task(get('baidu', 3))
        task2 = asyncio.create_task(get('douyin', 1))
        await task1
        await task2

    @utils.aruntime
    async def cpu_main(self):
        task3 = asyncio.create_task(get('baidu', 1))
        task1 = asyncio.create_task(acpu_task())
        task2 = asyncio.create_task(acpu_task())

        await task1
        await task2
        await task3

    def main(self):
        asyncio.run(self.cpu_main())
        asyncio.run(self.io_main())


if __name__ == '__main__':
    # t1 = Tutorial01()
    # t1.main()

    # t2 = Tutorial02()
    # t2.main()

    # t3 = Tutorial03()
    # t3.main()

    # t4 = Tutorial04()
    # t4.main()

    # t5 = Tutorial05()
    # t5.main()

    # t6 = Tutorial06()
    # t6.main()

    # t7 = Tutorial07()
    # t7.main()

    # t8 = Tutorial08()
    # t8.main()

    # t9 = Tutorial09()
    # t9.main()

    # t10 = Tutorial10()
    # t10.main()

    # t11 = Tutorial11()
    # t11.main()

    # t12 = Tutorial12()
    # t12.main()

    t13 = Tutorial13()
    t13.main()
