import requests
import json
import csv
import os

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
    global rows # 声明rows为全局变量
    try:
        content=text['data']['list']    # 热点精选
    except:
        content = text['data']  # 今日要闻和今日话题
    for item in content:
        source=item['url']
        title=item['title']
        rows.append((title,source))

if __name__ == '__main__':
    today_news_url='https://i.news.qq.com/trpc.qqnews_web.pc_base_srv.base_http_proxy/NinjaPageContentSync?pull_urls=news_top_2018'
    today_topic_url='https://i.news.qq.com/trpc.qqnews_web.pc_base_srv.base_http_proxy/NinjaPageContentSync?pull_urls=today_topic_2018'
    rows=[]
    # 获取今日要闻
    print("开始获取今日要闻>>>")
    rows.append(('以下为今日要闻',''))
    today_news=getPage(today_news_url)
    parse_news(today_news)
    print("...今日要闻获取完毕")
    # 获取今日话题
    print("开始获取今日话题>>>")
    rows.append(('以下为今日话题',''))
    today_topic=getPage(today_topic_url)
    parse_news(today_topic)
    print("...今日话题获取完毕")
    # 热点精选
    page = int(input("请输入你想获得的热点精选页数："))
    print("开始获取热点精选>>>")
    rows.append(('以下为热点精选',''))
    for i in range(page):
        hot_news_url = 'https://i.news.qq.com/trpc.qqnews_web.kv_srv.kv_srv_http_proxy/list?sub_srv_id=24hours&srv_id=pc&offset=' + str(
        i*20) + '&limit=20&strategy=1&ext={%22pool%22:[%22top%22],%22is_filter%22:7,%22check_type%22:true}'
        hot_news=getPage(hot_news_url)
        parse_news(hot_news)
        print("...第%d页获取完毕"%(i+1))
    with open('09_腾讯新闻.csv','a+',newline='') as f:  # newline=''可以消除每行后面的空行
        Csv_book=csv.writer(f)
        Csv_book.writerows(rows)
    print("保存完毕！路径为{}\\09_腾讯新闻.csv".format(os.getcwd()))
