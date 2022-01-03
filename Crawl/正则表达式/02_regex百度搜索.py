import requests
import re
from urllib import parse
import time

def getPage(url):
    try:
        re=requests.get(url)
        re.encoding=re.apparent_encoding
        # with open('02_regex_baidu.html','w',encoding='utf8') as f:
        #     f.write(re.text)
        return re.text
    except:
        print(re.status_code)
def parse_page(html):
    content=re.findall(r'{"?title"?:("|\')(.*?)("|\'),"?url"?:("|\')(.*?)("|\')}',html)
    # baike=re.findall(r'{title:\'(.*?)\',url:\'(.*?)\'}',html)
    # print(content)
    for item in content[:-1]:
        print("{}\n{}".format(item[1],item[4]))
    # 其他人都在搜
    try:
        everybody=re.findall(r'href="(/s.*?oq=)">([-_\w\u2e80-\u9fff]+)',html)
        print("其他人都在搜...")
        for item in everybody:
            e_href=parse.urljoin("http://www.baidu.com",item[0])
            e_title=item[1]
            print(e_title,e_href)

        # 第二种方法
        '''
        everybody2=re.finditer(r'href="(/s.*?oq=)">([-_\w\u2e80-\u9fff]+)',html)
        print("其他人都在搜...")
        for item in everybody2:
            e2_title=item.group(2)
            e2_url=parse.urljoin("http://www.baidu.com",item.group(1))
            print(e2_title,e2_url)
        '''
    except:
        pass

if __name__ == '__main__':
    word=parse.quote(input("请输入关键字："))
    pn=int(input("请输入想爬取的页数："))
    for i in range(pn):
        print("开始爬取第%d页>>>"%(i+1))
        url=f"http://www.baidu.com/s?wd={word}&pn={i*10}"
        html=getPage(url)
        parse_page(html)
        time.sleep(2)