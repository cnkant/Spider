import requests
from bs4 import BeautifulSoup
import asyncio
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
from urllib import parse

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'Referer': 'https://www.qiushibaike.com/'
}

def crawl(i):
    print('i的值为：',i)
    url='https://www.qiushibaike.com/8hr/page/{}/'.format(i)
    html=requests.get(url,headers=headers)
    print("第{}页".format(i))
    soup=BeautifulSoup(html.text,'lxml')
    lis=soup.select('.recmd-content')
    for li in lis:
        title=li.get_text()
        href=parse.urljoin('https://www.qiushibaike.com/',li['href'])
        print(title)
        print(href)

async def main():
    loop=asyncio.get_event_loop()
    tasks=[]
    with ThreadPoolExecutor(max_workers=10) as t:
        for i in range(1,11):
            # 三个参数：在哪执行、执行什么、执行对象
            tasks.append(loop.run_in_executor(t,crawl,i))

if __name__ == '__main__':
    loop=asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
