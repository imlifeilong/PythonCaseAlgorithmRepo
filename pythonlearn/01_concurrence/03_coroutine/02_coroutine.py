import asyncio


async def long_running_task():
    # 模拟一个耗时的异步任务
    print('任务开始...')
    await asyncio.sleep(10)  # 假设这里有一些耗时的IO操作
    print('任务结束')
    return '结果'


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


if __name__ == '__main__':
    # t8 = Tutorial08()
    # t8.main()

    # t9 = Tutorial09()
    # t9.main()

    t10 = Tutorial10()
    t10.main()
