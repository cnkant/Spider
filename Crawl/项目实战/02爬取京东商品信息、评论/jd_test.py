import requests
import re

headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    # 'referer': 'https://search.jd.com/Search?keyword=python&suggest=1.his.0.0&wq=python&page=1'
}

url='https://club.jd.com/comment/getProductPageFoldComments.action?callback=jQuery9287224&productId=13045700&score=0&sortType=5&page=0&pageSize=10'

res=requests.get(url,headers=headers)
res.encoding=res.apparent_encoding
print(res.text)

start=res.text.find('jQuery9287224(')+len('jQuery9287224(')
end=res.text.find(');')
print(res.text[start:end])  # 切片