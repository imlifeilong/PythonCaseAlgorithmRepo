import asyncio
import random
import uuid


class SeFuture:
    def __init__(self):
        self._ready_event = asyncio.Event()
        self.result = None

    async def wait(self, timeout=None, raise_exc: bool = False) -> None:
        # 等待结果
        result = await asyncio.wait_for(self._ready_event.wait(), timeout=timeout)

        if result is False:
            raise asyncio.TimeoutError()

        if raise_exc:
            raise RuntimeError(f'Error')

    async def set_result(self, result):
        self.result = result
        self._ready_event.set()  # 通知结果已经完成停止等待


class SeSocket:
    data = None

    def send(self, msg, mid):
        self.data = {"data": random.random(), "msg": msg, "id": mid}

    def recv(self):
        return self.data


class SeClient:
    data = None
    futures = {}
    mid = None
    stop_event = asyncio.Event()

    def __init__(self):
        self.sesocket = SeSocket()

    async def _send(self, msg):
        loop = asyncio.get_running_loop()
        # 将同步函数包装为异步协程
        loop.run_in_executor(None, self.sesocket.send, msg, self.mid)
        # self.data = {"data": random.random(), "msg": msg, "id": self.mid}

    async def _recv(self):
        await asyncio.sleep(random.random())
        loop = asyncio.get_running_loop()
        result = await loop.run_in_executor(None, self.sesocket.recv)

        return result

    async def recv(self):
        while not self.stop_event.is_set():
            result = await self._recv()
            # print("recv:", result)
            if result:
                await self.futures.get(self.mid).set_result(result)

    async def send(self, msg):
        future = SeFuture()
        self.mid = uuid.uuid4().hex
        self.futures[self.mid] = future
        await self._send(msg)
        await future.wait()

        return future.result

    async def start(self):
        recv_task = asyncio.create_task(self.recv())

    async def stop(self):
        self.stop_event.set()


async def amain():
    c = SeClient()
    await c.start()
    for i in range(10):
        result = await c.send(i)
        print(i, result)
        # if i == 5:
        #     await c.stop()


if __name__ == '__main__':
    asyncio.run(amain())
