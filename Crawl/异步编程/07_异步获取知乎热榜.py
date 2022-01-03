import asyncio
import json
import re
import aiohttp

headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'referer': 'https://www.baidu.com/s?tn=02003390_43_hao_pg&isource=infinity&iname=baidu&itype=web&ie=utf-8&wd=%E7%9F%A5%E4%B9%8E%E7%83%AD%E6%A6%9C'
}
async def getPages(url):
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as resp:
            print(resp.status)  # 打印状态码
            html=await resp.text()

    regex=re.compile('"hotList":(.*?),"guestFeeds":')
    text=regex.search(html).group(1)
    # print(json.loads(text))   # json换成字典格式
    for item in json.loads(text):
        title=item['target']['titleArea']['text']
        question=item['target']['excerptArea']['text']
        hot=item['target']['metricsArea']['text']
        link=item['target']['link']['url']
        img=item['target']['imageArea']['url']
        if not img:
            img='No Img'
        if not question:
            question='No Abstract'
        print("Title：{}\nPopular：{}\nQuestion：{}\nLink：{}\nImg：{}".format(title,hot,question,link,img))

if __name__ == '__main__':
    url='https://www.zhihu.com/billboard'
    loop=asyncio.get_event_loop()
    loop.run_until_complete(getPages(url))
    loop.close()
