# 不能爬太快！！！不然获取不到评论
from bs4 import BeautifulSoup
import requests
from urllib import parse
import csv,json,re
import threadpool
import time
from jd_mysqldb import Goods,Comments,sess_db

headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'Cookie': '__jdv=76161171|baidu|-|organic|%25E4%25BA%25AC%25E4%25B8%259C|1613711947911; __jdu=16137119479101182770449; areaId=7; ipLoc-djd=7-458-466-0; PCSYCityID=CN_410000_0_0; shshshfpa=07383463-032f-3f99-9d40-639cb57c6e28-1613711950; shshshfpb=u8S9UvxK66gfIbM1mUNrIOg%3D%3D; user-key=153f6b4d-0704-4e56-82b6-8646f3f0dad4; cn=0; shshshfp=9a88944b34cb0ff3631a0a95907b75eb; __jdc=122270672; 3AB9D23F7A4B3C9B=SEELVNXBPU7OAA3UX5JTKR5LQADM5YFJRKY23Z6HDBU4OT2NWYGX525CKFFVHTRDJ7Q5DJRMRZQIQJOW5GVBY43XVI; jwotest_product=99; __jda=122270672.16137119479101182770449.1613711948.1613738165.1613748918.4; JSESSIONID=C06EC8D2E9384D2628AE22B1A6F9F8FC.s1; shshshsID=ab2ca3143928b1b01f6c5b71a15fcebe_5_1613750374847; __jdb=122270672.5.16137119479101182770449|4.1613748918',
    'Referer': 'https://www.jd.com/'
}

num=0   # 商品数量
comments_num=0   # 评论数量

# 获取商品信息和SkuId
def getIndex(url):
    session=requests.Session()
    session.headers=headers
    global num
    res=session.get(url,headers=headers)
    print(res.status_code)
    res.encoding=res.apparent_encoding
    soup=BeautifulSoup(res.text,'lxml')
    items=soup.select('li.gl-item')
    for item in items[:2]:  # 爬取2个商品测试
        title=item.select_one('.p-name a em').text.strip().replace(' ','')
        price=item.select_one('.p-price strong').text.strip().replace('￥','')
        try:
            shop=item.select_one('.p-shopnum a').text.strip()   # 获取书籍时查找店铺的方法
        except:
            shop=item.select_one('.p-shop a').text.strip()  #   获取其他商品时查找店铺的方法
        link=parse.urljoin('https://',item.select_one('.p-img a').get('href'))
        SkuId=re.search('\d+',link).group()
        headers['Referer'] = f'https://item.jd.com/{SkuId}.html'
        headers['Connection'] = 'keep-alive'
        comments_num=getCommentsNum(SkuId,session)
        print(SkuId,title, price, shop, link, comments_num)
        print("开始将商品存入数据库...")
        try:
            IntoGoods(SkuId,title, price, shop, link, comments_num)
        except Exception as e:
            print(e)
            sess_db.rollback()
            print('rollback!')
        num += 1
        print("正在获取评论...")
        # 获取评论总页数
        url1 = f'https://club.jd.com/comment/productPageComments.action?productId={SkuId}&score=0&sortType=5&page=0&pageSize=10'
        res2 = session.get(url1,headers=headers)
        res2.encoding = res2.apparent_encoding
        json_data = json.loads(res2.text)
        max_page = json_data['maxPage']  # 经测试最多可获取100页评论，每页10条
        print("{}评论共{}页".format(SkuId,max_page))
        if max_page==0:
            IntoComments(SkuId,'0')
        else:
            for i in range(0, max_page):
                # 使用此链接获取评论得到的为json格式
                url2 = f'https://club.jd.com/comment/productPageComments.action?productId={SkuId}&score=0&sortType=5&page={i}&pageSize=10'
                # 使用此链接获取评论得到的非json格式，需要提取
                # url2_2=f'https://club.jd.com/comment/productPageComments.action?callback=jQuery9287224&productId={SkuId}&score=0&sortType=5&page={i}&pageSize=10'
                print("开始获取第{}页评论:{}".format(i+1,url2) )
                getComments(session,SkuId,url2)
                time.sleep(1)

# 获取评论总数量
def getCommentsNum(SkuId,sess):
    url=f'https://club.jd.com/comment/productCommentSummaries.action?referenceIds={SkuId}'
    res=sess.get(url)
    try:
        res.encoding=res.apparent_encoding
        json_data=json.loads(res.text)  # json格式转为字典
        num=json_data['CommentsCount'][0]['CommentCount']
        return num
    except:
        return 'Error'

# 获取评论
def getComments(sess,SkuId,url2):
    global comments_num
    res2 = sess.get(url2)
    res2.encoding=res2.apparent_encoding
    json_data=res2.text
    '''
    # 如果用url2_2需要进行如下操作提取json
    start = res2.text.find('jQuery9287224(') + len('jQuery9287224(')
    end = res2.text.find(');')
    json_data=res2.text[start:end]
    '''
    dict_data = json.loads(json_data)
    comments=dict_data['comments']
    for item in comments:
        comment=item['content'].replace('\n','')
        # print(comment)
        comments_num+=1
        try:
            IntoComments(SkuId,comment)
        except Exception as e:
            print(e)
            sess_db.rollback()
            print("rollback！")

# 商品信息入库
def IntoGoods(SkuId,title, price, shop, link, comments_num):
    goods_data=Goods(
        sku_id=SkuId,
        name=title,
        price=price,
        comments_num=comments_num,
        shop=shop,
        link=link
    )
    sess_db.add(goods_data)
    sess_db.commit()
    print('commit')

# 评论入库
def IntoComments(SkuId,comment):
    comments_data=Comments(
        sku_id=SkuId,
        comments=comment
    )
    sess_db.add(comments_data)
    sess_db.commit()
    print('commit')

if __name__ == '__main__':
    start_time=time.time()
    urls=[]
    KEYWORD=parse.quote(input("请输入要查询的关键词："))
    for i in range(1,2):    # 爬取一页进行测试
        url=f'https://search.jd.com/Search?keyword={KEYWORD}&wq={KEYWORD}&page={i}'
        urls.append(([url,],None))  # threadpool要求必须这样写
    pool=threadpool.ThreadPool(2)  # 2个线程的线程池
    reque=threadpool.makeRequests(getIndex,urls)    # 创建任务
    for r in reque:
        pool.putRequest(r)  # 向线程池提交任务
    pool.wait() # 等待所有任务执行完毕
    print("共获取{}件商品，获得{}条评论，耗时{}".format(num,comments_num,time.time()-start_time))
