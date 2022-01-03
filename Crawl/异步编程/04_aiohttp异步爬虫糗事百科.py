from bs4 import BeautifulSoup
import aiohttp  # 代替requests
import asyncio
from urllib import parse

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'Referer': 'https://www.qiushibaike.com/'
}

async def getPage(i):
    print('i的值为：',i)
    url='https://www.qiushibaike.com/8hr/page/{}/'.format(i)
    async  with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as resp:
            print(resp.status)  # 打印状态码
            print('第{}页'.format(i))
            html=await resp.text()
    soup=BeautifulSoup(html,'lxml')
    lis=soup.select('.recmd-content')
    for li in lis:
        title=li.get_text()
        href=parse.urljoin('https://www.qiushibaike.com/',li['href'])
        print(title)
        print(href)

if __name__ == '__main__':
    loop=asyncio.get_event_loop()   # 获取事件循环
    tasks=[getPage(i) for i in range(1,11)] # 创建任务
    loop.run_until_complete(asyncio.wait(tasks))    # 执行任务
    loop.close()    # 执行之后关闭
