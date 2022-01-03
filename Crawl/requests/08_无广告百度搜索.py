import requests
from urllib import parse
from bs4 import BeautifulSoup
import time

headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

def getPage(url):
    try:
        re=requests.get(url,headers=headers)
        re.encoding=re.apparent_encoding
        return re.text
    except:
        print(re.status_code)

def parsePage(text):
    soup=BeautifulSoup(text,'lxml')
    content=soup.select('div .result')
    for item in content:
        try:
            title=item.select('h3 a')[0].text
            href=item.select('h3 a')[0]['href']
            abstract=item.select('.c-abstract')[0].text
            print("{}-{}\n{}".format(title,abstract,href))
        except:
            pass
    # baike
    try:
        bk=soup.select("div .result-op .op-bk-polysemy-piccontent")[0]
        baike_abstract=bk.select('p')[0].text.strip()
        baike_title=soup.select('.result-op .c-gap-bottom-small a')[0].text.strip()
        baike_href=soup.select('.result-op .c-gap-bottom-small a')[0]['href']
        print("{}-{}\n{}".format(baike_title,baike_abstract,baike_href))
    except:
        pass

    # 其他人还在搜
    try:
        items=soup.select("div .result-op .list_1V4Yg a")
        print("其他人还在搜>>>")
        for item in items:
            e_title=item.text
            e_href=parse.urljoin('http://www.baidu.com',item['href'])
            print(e_title,e_href)
    except:
        pass

if __name__ == '__main__':
    word=parse.quote(input('请输入关键字：'))
    pn=int(input("请输入爬取的页数："))
    for i in range(pn):
        print("开始爬取第%d页>>>"%(i+1))
        url=f'http://www.baidu.com/s?wd={word}&pn={i*10}'
        text=getPage(url)
        parsePage(text)
        time.sleep(2)
