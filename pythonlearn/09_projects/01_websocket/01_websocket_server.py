import asyncio
import json
import random
import time

import websockets


async def echo(websocket, path):
    async for message in websocket:
        print(f"Received message: {message}")
        data = json.loads(message)
        data['data'] = {"action": "pong", "ts": time.time()}
        # 将接收到的消息发回给客户端
        await websocket.send(json.dumps(data))

        other_data = data.copy()
        other_data['id'] = time.time()
        await websocket.send(json.dumps(other_data))
        other_data['id'] = time.time()
        await websocket.send(json.dumps(other_data))


async def main():
    # 启动 WebSocket 服务器
    server = await websockets.serve(echo, "localhost", 8765)
    print("WebSocket server started on ws://localhost:8765")

    # 保持服务器运行
    await server.wait_closed()


# 启动服务器
asyncio.run(main())
