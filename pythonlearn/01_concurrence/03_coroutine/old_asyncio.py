import asyncio


@asyncio.coroutine
def func1():
    print(1)
    # 网络 IO 请求
    yield from asyncio.sleep(2)  # 遇到 IO 耗时操作，自动切换
    print(2)


@asyncio.coroutine
def func2():
    print(3)
    # 网络 IO 请求
    yield from asyncio.sleep(2)  # 遇到 IO 耗时操作，自动切换
    print(4)


tasks = [
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2())
]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
