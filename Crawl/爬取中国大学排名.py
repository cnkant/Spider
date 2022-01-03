import requests
from bs4 import BeautifulSoup
import bs4
url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html"
ulist = []


# 获取HTML页面
def getHTML(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("异常")
        return ""

# 提取排名信息
def getUniv(ulist, html):
    soup = BeautifulSoup(html, "html.parser")

    for tr in soup.tbody.children:
        if isinstance(tr, bs4.element.Tag):  # tr是bs4语句
            tds = tr('td')
            ulist.append(
                [tds[0].string, tds[1].string, tds[2].string, tds[3].string])
    return ulist

# 输出排名信息
def readUniv(ulist):
    s = eval(input("请输入要查询前多少名大学："))
    print("前{}名的排名如下：".format(s))
    print("{:^3}\t{:^20}\t{:^10}\t{:^5}".format("排名", "学校名称", "城市", "分数"))
    for i in range(s):
        u = ulist[i]
        print("{:^3}\t{:^20}\t{:^10}\t{:^5}".format(u[0], u[1], u[2], u[3]))


html = getHTML(url)
ulist = getUniv(ulist, html)
readUniv(ulist)