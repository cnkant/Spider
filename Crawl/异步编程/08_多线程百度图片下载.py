import requests
from urllib import parse
from uuid import uuid4
import os
import threading
import time
from concurrent.futures import ThreadPoolExecutor

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
}
session=requests.session()
session.headers=headers
num=0
def getPage(url):
    # 多线程耗时0.7709999084472656
    # 线程池耗时0.7650001049041748
    ThreadPool=ThreadPoolExecutor(max_workers=5)
    page=session.get(url)
    print(page.status_code)
    # print(page.json())
    page.encoding=page.apparent_encoding
    data=page.json()['data']    # 列表
    for i in data[:-1]: # 因为最后一个是空的，所以取到倒数第二个元素
        img_url=i['hoverURL']
        print(img_url)
        # imgDownload(img_url)

        # 多线程
        # t = threading.Thread(target=imgDownload,args=(img_url,))
        # t.start()

        # 线程池
        ThreadPool.submit(imgDownload,img_url)

# 下载图片
def imgDownload(url):
    try:
        if not os.path.exists('08_BaiduImgs'):
            os.makedirs('08_BaiduImgs')
    except FileExistsError:
        pass
    global num
    content=session.get(url)
    with open('08_BaiduImgs/{}.jpg'.format(uuid4()),'wb') as f:
        for chunk in content.iter_content(225): # 每次下载225字节
            if chunk:
                f.write(chunk)
        # num += 1
        # print(">>>第{}张爬取成功.".format(num))

if __name__ == '__main__':
    # num=0
    word=input("请输入关键词：")
    pages=input("请输入要爬取的页数，每页30张图片：")
    s=time.time()
    for page in range(int(pages)):
        url='https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&word='+parse.quote(word)+'&pn='+str((page+1)*30)
        getPage(url)
    print('耗时{}'.format(time.time()-s))
