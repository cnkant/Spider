import requests
from bs4 import BeautifulSoup


def bianliSoup(url):

    r = requests.get(url, timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    demo = r.text
    soup = BeautifulSoup(demo, "html.parser")
    # 子节点列表，contents为列表类型
    print("子节点列表：")
    print(soup.head.contents)  # 输出head标签的子节点内容
    print(soup.body.contents)  # 输出body标签的子节点内容
    print(len(soup.body.contents))  # 输出body标签的子节点数量
    print(soup.body.contents[1])  # 输出第一个子节点内容
    # 儿子节点列表，childern和descendants为迭代类型，只能用在for循环之中
    print("遍历儿子节点：")  # 与contents类似，区别是children为遍历儿子节点
    for child in soup.body.childern:
        print(child)
    # 子孙节点列表
    print("子孙节点列表：")  # 包含所有子孙节点列表
    for child in soup.body.descendants:
        print(child)


url = "https://python123.io/ws/demo.html"
bianliSoup(url)
