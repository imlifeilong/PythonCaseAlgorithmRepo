import asyncio


class AIO:
    async def get(self):
        print("get 要进行IO了，先让出执行权限")
        # 网络 IO 请求
        await asyncio.sleep(3)  # 遇到 IO 耗时操作，自动切换
        print("get IO执行完了，切换回来")

    async def put(self):
        print("put 要进行IO了，先让出执行权限")
        # 网络 IO 请求
        await asyncio.sleep(2)  # 遇到 IO 耗时操作，自动切换
        print("put IO执行完了，切换回来")

    async def post(self):
        print("post 要进行IO了，先让出执行权限")
        # 网络 IO 请求
        await asyncio.sleep(1)  # 遇到 IO 耗时操作，自动切换
        print("post IO执行完了，切换回来")

    async def delete(self):
        print("delete 要进行IO了，先让出执行权限")
        # 网络 IO 请求
        await asyncio.sleep(1)  # 遇到 IO 耗时操作，自动切换
        print("delete IO执行完了，切换回来")

    def main(self):
        tasks = [
            asyncio.ensure_future(self.get()),
            asyncio.ensure_future(self.put()),
            asyncio.ensure_future(self.post()),
            self.delete(),

        ]
        # 获取当前上下文中的事件循环，每个线程可以有自己独立的事件循环，
        # 主线程在程序开始时，会创建并共享一个事件循环
        # 在 Python 3.7 及以后的版本中，如果你没有显式地设置事件循环，
        # asyncio.get_event_loop() 会在主线程中自动创建一个新的事件循环（如果尚不存在的话）
        # 不推荐在多线程环境中共享事件循环，因为这可能会导致难以追踪的错误和竞争条件。

        loop = asyncio.get_event_loop()
        # asyncio.wait 是一个协程，它会在事件循环中被调用并等待所有给定的任务完成。
        # loop.run_until_complete(future) 方法用于运行事件循环直到给定的 Future 或 coroutine 完成
        #
        loop.run_until_complete(asyncio.wait(tasks))


if __name__ == '__main__':
    aio = AIO()
    aio.main()
