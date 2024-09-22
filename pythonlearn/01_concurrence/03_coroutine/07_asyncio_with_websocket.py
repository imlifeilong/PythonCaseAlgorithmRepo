import asyncio
import websockets
import json
import uuid


class WebSocketClient:
    def __init__(self, uri):
        self.uri = uri
        self.futures = {}  # 用于存储消息ID对应的Future对象

    async def connect(self):
        # 连接到WebSocket服务器
        self.websocket = await websockets.connect(self.uri)
        # 启动接收消息的任务
        asyncio.create_task(self.receive_messages())

    async def send_message(self, message):
        # 生成唯一的消息ID
        message_id = str(uuid.uuid4())
        # 包装消息，包括消息ID
        message_with_id = json.dumps({
            'id': message_id,
            'data': message
        })

        # 创建一个Future对象，等待响应
        future = asyncio.get_event_loop().create_future()
        self.futures[message_id] = future

        # 发送消息
        await self.websocket.send(message_with_id)

        # 返回Future对象，供调用方等待响应
        return future

    async def receive_messages(self):
        # 持续接收服务器的消息
        async for message in self.websocket:
            print(message)
            data = json.loads(message)
            message_id = data.get('id')
            # 查找对应的Future对象
            if message_id in self.futures:
                future = self.futures.pop(message_id)
                # 设置Future为已完成状态，并返回数据
                if not future.done():
                    future.set_result(data.get('data'))

    async def close(self):
        await self.websocket.close()


# 测试客户端
async def main():
    ws_client = WebSocketClient('ws://localhost:8765')  # 替换成实际WebSocket地址
    await ws_client.connect()

    # 发送消息并等待异步响应
    future = await ws_client.send_message({'action': 'ping'})
    response = await future  # 等待服务器的响应
    print(f"Received response: {response}")

    await ws_client.close()


# 运行客户端
asyncio.run(main())
