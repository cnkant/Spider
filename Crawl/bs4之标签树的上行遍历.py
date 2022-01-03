import requests
from bs4 import BeautifulSoup
url = "https://python123.io/ws/demo.html"
r = requests.get(url, timeout=30)
r.encoding = r.apparent_encoding
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
# 父节点
print(soup.title.parent)
print(soup.html.parent)  # 最高层，父节点为本身
print(soup.parent)  # soup父节点为None
# 遍历先辈节点，迭代类型，只能用在for循环之中
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print("父节点名称为：")
        print(parent.name)