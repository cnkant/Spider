import time
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import requests
from urllib import parse

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'Referer': 'https://www.qiushibaike.com/'
}
def crawl(i,q):
    print(q)
    url='https://www.qiushibaike.com/8hr/page/{}/'.format(i)
    # print(url)
    html=requests.get(url,headers=headers)
    # print(html.status_code)
    print("第{}页".format(i))
    soup=BeautifulSoup(html.text,'lxml')
    lis=soup.select('.recmd-content')
    for li in lis:
        title=li.get_text()
        href=parse.urljoin('https://www.qiushibaike.com/',li['href'])
        print(title)
        print(href)

if __name__ == '__main__':
    s=time.time()
    with ThreadPoolExecutor(max_workers=10) as t:
        for i in range(1,11):
            args = [i,i+1]
            t.submit(lambda p:crawl(*p) ,args)
        # futures=[t.submit(crawl,i) for i in range(1,11)]
    print('线程池运行时间：',time.time()-s)
