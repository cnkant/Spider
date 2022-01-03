import asyncio

# async表这是一个异步函数
async def net():
    print('12')

async def main():
    # net()   # 这样调用会出错
    await net()    # await等待异步函数返回

asyncio.run(main())
