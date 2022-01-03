import requests
from bs4 import BeautifulSoup
import multiprocessing
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
# 线程中执行
def get_html(url):
    print("获取当前书的线程的父进程为{}".format(multiprocessing.current_process().pid))
    html=requests.get(url,headers=headers)
    soup=BeautifulSoup(html.text,'lxml')
    title=soup.select('h1 span')[0].text
    print(title)

# 进程中执行
def get_link(url):
    print(url)
    print("当前进程pid为{}".format(multiprocessing.current_process().pid))
    html=requests.get(url,headers=headers)
    print(html.status_code)
    # 创建线程池，最大三个任务
    threadpools=ThreadPoolExecutor(max_workers=3)
    soup=BeautifulSoup(html.text,'lxml')
    links=soup.select('.info h2 a')
    for link in links:
        url1=link['href']
        threadpools.submit(get_html,url1)

if __name__ == '__main__':
    # 爬取小说、历史、旅行三个分类
    urls=[
        'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4',
        'https://book.douban.com/tag/%E5%8E%86%E5%8F%B2',
        'https://book.douban.com/tag/%E6%97%85%E8%A1%8C'
    ]
    # 开启三个进程
    with ProcessPoolExecutor(max_workers=3) as executor:
       futures=[executor.submit(get_link,url) for url in urls]
