import requests

url='http://seowyc.com/seo/api/wyc.html'
data={
    'content':'其实市面上有很多的伪原创接口，但是许多接口都是收费的，最近在搜索时找到一个免费的接口感觉挺不错的推荐给大家。',
    'ratio': 100
}
req=requests.post(url,data=data)
print(req.text)