import asyncio
import json
import time

import websockets
import logging

LOGGER = logging.getLogger(__name__)


class Tab:
    def __init__(self, wsurl):
        self.wsurl = wsurl
        self._connected = False
        self._ws = None
        self._events = {}
        self._next_id = 0
        self._recv_task = None
        self._event_callbacks = {}

    async def connect(self):
        if self._connected:
            return

        self._ws = await websockets.connect(self.wsurl)
        self._connected = True
        self._recv_task = asyncio.create_task(self._recv_loop())

    async def _recv_loop(self):
        while self._connected:
            try:
                data = await self._ws.recv()  # 使用异步的接收数据
                self._handle_message(data)
            except websockets.ConnectionClosed:
                LOGGER.info("WebSocket connection closed")
                break
            except Exception as e:
                LOGGER.exception("Exception in recv_loop: %s", e)
                break

    def _handle_message(self, data):
        message = json.loads(data)
        LOGGER.debug("Received message: %s", message)
        if 'id' in message:
            # 处理 response
            if message['id'] in self._events:
                self._events[message['id']] = message
        elif 'method' in message:
            # 处理事件
            event_name = message['method']
            if event_name in self._event_callbacks:
                for callback in self._event_callbacks[event_name]:
                    asyncio.create_task(callback(message))

    async def send(self, method, params=None):
        message = {
            "id": self._next_message_id(),
            "method": method,
            "params": params or {}
        }
        await self._ws.send(json.dumps(message))
        LOGGER.debug("Sent message: %s", message)

    async def _wait_event(self, event_name, timeout=None):
        start_time = time.time()
        while event_name not in self._events:
            if timeout and time.time() - start_time > timeout:
                raise TimeoutError(f"Event {event_name} timed out")
            await asyncio.sleep(0.01)  # 异步等待避免阻塞

    def add_event_listener(self, event_name, callback):
        if event_name not in self._event_callbacks:
            self._event_callbacks[event_name] = []
        self._event_callbacks[event_name].append(callback)

    def _next_message_id(self):
        self._next_id += 1
        return self._next_id

    async def close(self):
        if self._connected:
            await self._ws.close()
            self._connected = False
        if self._recv_task:
            await self._recv_task


async def on_event(message):
    print("Received event:", message)


async def main():
    tab = Tab("ws://localhost:9222/devtools/page/123")
    await tab.connect()

    # 添加事件监听器
    tab.add_event_listener("Page.loadEventFired", on_event)

    # 发送命令
    await tab.send("Page.enable")

    # 等待某个事件触发
    await tab._wait_event("Page.loadEventFired", timeout=5)

    # 关闭连接
    await tab.close()


if __name__ == "__main__":
    asyncio.run(main())
