import requests
from bs4 import BeautifulSoup
from urllib import parse
from _DoubanDB import Douban,session


headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
'Cookie': 'bid="l0z/t08D0Ts"; douban-fav-remind=1; ll="118243"; _vwo_uuid_v2=D92529FAF20FCCBDFD9EE7142CCF2A27B|86cf248d8fa2f1176a0dceca9a648284; _ga=GA1.2.439071017.1588390970; viewed="4006425"; gr_user_id=ece586e7-f73d-4ec7-9223-dc7f86a1b88f; __yadk_uid=PHY1JWQiEXUd01vLIDHvqdV1BolquoRC; __gads=ID=3fa1a30c35871e51-22fb8d8d1fc200e6:T=1592114861:RT=1592114861:R:S=ALNI_Ma14g7W6UhDDK2G7GXNcY0Y_dDlqw; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=12902ac3-3c38-4add-b44f-bf6932df64be; gr_cs1_12902ac3-3c38-4add-b44f-bf6932df64be=user_id%3A0; _pk_ref.100001.3ac3=%5B%22%22%2C%22%22%2C1612099229%2C%22https%3A%2F%2Fwww.baidu.com%2Fs%3Fie%3Dutf-8%26f%3D8%26rsv_bp%3D1%26ch%3D%26tn%3D02003390_43_hao_pg%26bar%3D%26wd%3D%25E8%25B1%2586%25E7%2593%25A3%25E8%25AF%25BB%25E4%25B9%25A6%26oq%3D%2525E8%2525B1%252586%2525E7%252593%2525A3%2525E7%252586%25259F%2525E8%2525AF%2525BB%26rsv_pq%3Db009334e0024afd9%26rsv_t%3D87a3LbHT%252FA6%252FJXVxnKB2vHEO3BP3BZ%252FQNgKih67p%252F5poDWyHQ2T4Kw0ohOciuh294Ei5nlDSCSvt%26rqlang%3Dcn%26rsv_enter%3D1%26rsv_btype%3Dt%26rsv_dl%3Dtb%26inputT%3D1431%22%5D; _pk_ses.100001.3ac3=*; ap_v=0,6.0; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_12902ac3-3c38-4add-b44f-bf6932df64be=true; __utma=30149280.439071017.1588390970.1611392728.1612099231.16; __utmc=30149280; __utmz=30149280.1612099231.16.15.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=%E8%B1%86%E7%93%A3%E8%AF%BB%E4%B9%A6; __utmt_douban=1; __utma=81379588.439071017.1588390970.1598167798.1612099231.2; __utmc=81379588; __utmz=81379588.1612099231.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=%E8%B1%86%E7%93%A3%E8%AF%BB%E4%B9%A6; __utmt=1; __utmb=30149280.16.10.1612099231; __utmb=81379588.16.10.1612099231; _pk_id.100001.3ac3=640825538b9c92bf.1598167799.2.1612099753.1598167799.'
}

def getPage(url):
    try:
        re=requests.get(url,headers=headers)
        re.encoding=re.apparent_encoding
        return re.text
    except:
        print(re.status_code)

def parsePage(soup):
    info=soup.select('.info')
    for item in info:
        title=item.select('h2')[0].text.replace(' ','').replace('\n','')
        about=item.select('.pub')[0].text.replace(' ','').replace('\n','')
        star=item.select('.rating_nums')[0].text.replace(' ','').replace('\n','')
        comments=item.select('.pl')[0].text.replace(' ','').replace('\n','').replace('(','').replace(')','')
        abstract=item.select('p')[0].text.replace(' ','').replace('\n','')
        print(title,about,star,comments)
        print('-'*50)
        print(abstract)
        try:
            intoDB(title,about,star,comments,abstract)  # 存入数据库
        except Exception as e:
            print(e)    # 输出错误声明
            session.rollback()  # 回滚

def intoDB(title,about,star,comments,abstract):
    data_douban=Douban(
        title=title,
        about=about,
        star=star,
        comments=comments,
        abstract=abstract
    )
    session.add(data_douban)
    session.commit()

if __name__ == '__main__':
    kw=parse.quote("编程")
    s_page=int(input("输入爬取的起始页数："))
    e_page=int(input("输入爬取的最后页数："))
    for i in range(s_page-1,e_page):
        url=f'https://book.douban.com/tag/{kw}?start={i*20}&type=T'
        soup=BeautifulSoup(getPage(url),'lxml')
        parsePage(soup)
