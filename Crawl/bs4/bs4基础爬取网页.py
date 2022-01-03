import requests
from bs4 import BeautifulSoup


def getSOUP(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        # print(r.text)  # 代码很乱
        soup = BeautifulSoup(r.text, "html.parser")  # parser分析器、解析器
        # print(soup.prettify())   # 美化后的网页代码
        print(soup.a)  # 获取标签内容
        print(soup.a.name)  # 获取标签名字
        print(soup.a.parent.name)
        print(soup.a.parent.parent.name)
        tag = soup.a
        print(type(tag))  # tag属性
        print(tag.attrs)  # 打印属性,无论存在属性都会返回一个字典类型
        print(type(tag.attrs))  # 打印属性类型
        print(tag.attrs['class'])  # 打印class属性的属性值
        print(type(tag.attrs['class']))
        print(tag.string)  # 获取字符串
    except expression as identifier:
        print("错误")


if __name__ == "__main__":
    url = "https://python123.io/ws/demo.html"
    getSOUP(url)
