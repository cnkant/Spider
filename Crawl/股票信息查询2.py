import requests
from bs4 import BeautifulSoup
import re


# 获得HTML页面
def getHTMLpages(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


# 将股票信息存入列表
def getSharelist(ulis, html):
    soup = BeautifulSoup(html, "html.parser")
    tags = soup.find_all('a', target="_blank")
    # print(tags)
    for tag in tags:
        str1 = tag.attrs['href']  # 获得链接信息
        # print(type(str1))
        # print(str1)
        match = re.search(r's[hz]\d{6}', str1)  # 从链接中找到股票代码
        if match:  # 必须加判断，因为有的链接不符合，这样的话正则表达式匹配不到，match.group(0)就是空的，会报错TypeError
            # print(match.group(0))
            ulis.append(match.group(0))
        else:
            continue


# 将个股信息存入文件
def getShareinfo(url, count):
    html = getHTMLpages(url)
    soup = BeautifulSoup(html, "html.parser")
    names = soup.find('h1', attrs={'class': 'name'})  #股票名称
    price = soup.find('span', attrs={'class': 'latest'})  # 个股价格
    # print(tags.attrs['class'])
    if names:  # 必须加判断，因为有的查询不到
        TestDict = {}
        # print(names.text) # 打印标签内的内容
        TestDict[names.text] = price.text
        # print(price.text)

        # 将股票信息追加写入到股票信息.txt中
        with open("D:\VscodePy\pytest\股票信息.txt", "a", encoding='utf-8') as f:
            f.write('\n' + str(TestDict))
            f.close()
        print("当前进度: {:.2f}%\n".format(count * 100 / len(ulis)), end="")


# 主函数
if __name__ == "__main__":
    ulis = []
    count = 1
    url1 = "http://quote.eastmoney.com/stock_list.html"
    html = getHTMLpages(url1)
    # with open("D:\VscodePy\pytest\sharehtml1.txt", "w", encoding='utf-8') as f:
    #     f.write(html)
    #     f.close()
    # with open('D:\VscodePy\pytest\sharehtml1.txt', 'r', encoding='utf-8') as f:
    #     sss = f.read()
    #     getSharelist(ulis, sss)
    #     f.close()
    # print(ulis)
    getSharelist(ulis, html)
    print("数据共有{}条\n".format(len(ulis)))
    url2 = "https://www.laohu8.com/stock/"
    for i in range(len(ulis)):
        code = re.search(r'\d{6}', ulis[i])
        url = url2 + code.group(0)
        getShareinfo(url, count)
        count += 1
