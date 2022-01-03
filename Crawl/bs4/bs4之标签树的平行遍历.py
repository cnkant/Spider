# 平行遍历的内容不一定是标签，还可能是string
import requests
from bs4 import BeautifulSoup
url = "https://python123.io/ws/demo.html"
r = requests.get(url, timeout=30)
r.encoding = r.apparent_encoding
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
# 上一个平行节点
print("上："+soup.a.previous_sibling) # a标签的上一个平行节点不一定是标签，可能是p标签的内容
print(soup.a.previous_sibling.previous_sibling) #上上一个平行节点，可能为空值
# 下一个平行节点
print("下"+soup.a.next_sibling)
print(soup.a.next_sibling.next_sibling)
# 遍历平行节点，迭代类型，只能用在for循环之中
print("之前")
for sibling in soup.a.previous_siblings: # 遍历a标签前面的平行节点
    print(sibling)
print("之后")
for sibling in soup.a.next_siblings: # 遍历a标签后面的平行节点
    print(sibling)
