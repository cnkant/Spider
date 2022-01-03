import requests
url1 = "http://www.baidu.com/s"  # 百度
url2 = "http://www.so.com/s"  # 360


def getHTMLText(url):
    try:
        if url == url1:
            kv = {'wd': "关键词"}
        else:
            kv = {'q': "关键词"}
        r = requests.get(url, params=kv, timeout=30)
        r.raise_for_status()  # 如果不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        print(r.request.url)
        print(len(r.text))
    except:
        print("爬取失败")


if __name__ == "__main__":
    print("百度：")
    getHTMLText(url1)
    print("360：")
    getHTMLText(url2)
