import requests
import re # 正则表达式库
from bs4 import BeautifulSoup
url = "https://python123.io/ws/demo.html"
r = requests.get(url, timeout=30)
r.encoding = r.apparent_encoding
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
# find_all:name、attrs、recursive、string、其他参数
# 标签名、标签属性值、是否检索子孙节点默认True、标签中字符串
# name
# 获取全部链接
for link in soup.find_all('a'):
    print(link.get("href"))
# 获取a和p标签内容
print("获取a和p标签内容")
print(soup.find_all(['a', 'p']))  # 列表形式
for s in soup.find_all(['a', 'p']):
    print(s)
# 获取soup的全部标签
print("全部标签名称")
for tag in soup.find_all(True):
    print(tag.name)
print("使用正则表达式查找以b开头的标签名称")
for tag in soup.find_all(re.compile('b')):
    print(tag.name)
# attrs
print("获取p标签中属性为course的内容")
print(soup.find_all('p', 'course'))
print("查找id为link1的内容")
print(soup.find_all(id='link1'))  # 若没有则返回空列表
print("使用正则表达式查找id以link开头的标签内容")
print(soup.find_all(id=re.compile("link")))
# recursive(递归的)
print(soup.find_all('a'))
print("测试recursive：")
print(soup.find_all('a', recursive=False))  # 为空，说明soup儿子节点无a标签
print(soup.find_all('a', recursive=True))
# string
print("查找Basic Python")
print(soup.find_all(string="Basic Python"))  # 没有输出空列表
print("使用正则表达式查找包含Python的内容：")
print(soup.find_all(string=re.compile("Python"))) # 区分大小写