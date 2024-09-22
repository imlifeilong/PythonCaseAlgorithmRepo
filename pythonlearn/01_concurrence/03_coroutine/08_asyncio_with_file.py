import asyncio
import aiofiles


async def async_read_file():
    async with aiofiles.open('logging.conf', 'r') as file:
        content = await file.read()
        print(content)


if __name__ == '__main__':
    asyncio.run(async_read_file())
