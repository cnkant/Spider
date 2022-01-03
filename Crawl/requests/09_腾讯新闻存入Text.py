import requests
import json

headers={
    'referer': 'https://news.qq.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

def getPage(url):
    try:
        re=requests.get(url,headers=headers)
        re.encoding=re.apparent_encoding
        return json.loads(re.text)
    except:
        print(re.status_code)

# 获取新闻
def parse_news(text):
    try:
        content=text['data']['list']    # 热点精选
    except:
        content = text['data']  # 今日要闻和今日话题
    for item in content:
        source=item['url']
        title=item['title']
        f.write("{}{}\n".format(title,source))

'''
# 获取热点精选
def parse_hot_news(text):
    content=text['data']['list']
    for item in content:
        source=item['url']
        title=item['title']
        f.write(title,source)
'''

if __name__ == '__main__':
    today_news_url='https://i.news.qq.com/trpc.qqnews_web.pc_base_srv.base_http_proxy/NinjaPageContentSync?pull_urls=news_top_2018'
    today_topic_url='https://i.news.qq.com/trpc.qqnews_web.pc_base_srv.base_http_proxy/NinjaPageContentSync?pull_urls=today_topic_2018'
    # 获取今日要闻
    print("开始获取今日要闻>>>")
    today_news=getPage(today_news_url)
    with open('09_腾讯新闻.txt', 'a+',encoding='utf-8') as f:
        f.write("今日要闻\n")
        parse_news(today_news)
    print("...今日要闻获取完毕")
    # 获取今日话题
    print("开始获取今日话题>>>")
    today_topic=getPage(today_topic_url)
    with open('09_腾讯新闻.txt', 'a+',encoding='utf8') as f:
        f.write("今日话题\n")
        parse_news(today_topic)
    print("...今日话题获取完毕")
    # 热点精选
    page = int(input("请输入你想获得的热点精选页数："))
    print("开始获取热点精选>>>")
    with open('09_腾讯新闻.txt', 'a+',encoding='utf8') as f:
        f.write("热点精选\n")
        for i in range(page):
            hot_news_url = 'https://i.news.qq.com/trpc.qqnews_web.kv_srv.kv_srv_http_proxy/list?sub_srv_id=24hours&srv_id=pc&offset=' + str(
            i*20) + '&limit=20&strategy=1&ext={%22pool%22:[%22top%22],%22is_filter%22:7,%22check_type%22:true}'
            hot_news=getPage(hot_news_url)
            parse_news(hot_news)
            print("...第%d页获取完毕"%(i+1))
    print("保存完毕！路径为{}\\09_腾讯新闻.txt".format(os.getcwd()))
