# 用session取代requests
# 解析库使用bs4
# 并发库使用concurrent
import requests
# from lxml import etree    # 使用xpath解析
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
from urllib import parse
from mysqldb import sess, House
import re
import time
import asyncio

headers = {
    'referer': 'https://zz.zu.fang.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'cookie': 'global_cookie=ffzvt3kztwck05jm6twso2wjw18kl67hqft; integratecover=1; city=zz; __utmc=147393320; ASP.NET_SessionId=vhrhxr1tdatcc1xyoxwybuwv; __utma=147393320.427795962.1613371106.1613575774.1613580597.6; __utmz=147393320.1613580597.6.5.utmcsr=zz.fang.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt_t0=1; __utmt_t1=1; __utmt_t2=1; Rent_StatLog=c158b2a7-4622-45a9-9e69-dcf6f42cf577; keyWord_recenthousezz=%5b%7b%22name%22%3a%22%e4%ba%8c%e4%b8%83%22%2c%22detailName%22%3a%22%22%2c%22url%22%3a%22%2fhouse-a014864%2f%22%2c%22sort%22%3a1%7d%2c%7b%22name%22%3a%22%e9%83%91%e4%b8%9c%e6%96%b0%e5%8c%ba%22%2c%22detailName%22%3a%22%22%2c%22url%22%3a%22%2fhouse-a0842%2f%22%2c%22sort%22%3a1%7d%2c%7b%22name%22%3a%22%e7%bb%8f%e5%bc%80%22%2c%22detailName%22%3a%22%22%2c%22url%22%3a%22%2fhouse-a014871%2f%22%2c%22sort%22%3a1%7d%5d; g_sourcepage=zf_fy%5Elb_pc; Captcha=6B65716A41454739794D666864397178613772676C75447A4E746C657144775A347A6D42554F446532357649643062344F6976756E563450554E59594B7833712B413579506C4B684958343D; unique_cookie=U_0l0d1ilf1t0ci2rozai9qi24k1pkl9lcmrs*14; __utmb=147393320.21.10.1613580597'
}
data={
    'agentbid':''
}

session = requests.session()
session.headers = headers

# 获取页面
def getHtml(url):
    res = session.get(url)
    if res.status_code==200:
        res.encoding = res.apparent_encoding
        return res.text
    else:
        print(res.status_code)

# 获取页面总数量
def getNum(text):
    soup = BeautifulSoup(text, 'lxml')
    txt = soup.select('.fanye .txt')[0].text
    # 取出“共**页”中间的数字
    num = re.search(r'\d+', txt).group(0)
    return num

# 获取详细链接
def getLink(url):
    text=getHtml(url)
    soup=BeautifulSoup(text,'lxml')
    links=soup.select('.title a')
    for link in links:
        href=parse.urljoin('https://zz.zu.fang.com/',link['href'])
        hrefs.append(href)

# 解析页面
def parsePage(url):
    res=session.get(url)
    if res.status_code==200:
        res.encoding=res.apparent_encoding
        soup=BeautifulSoup(res.text,'lxml')
        try:
            title=soup.select('div .title')[0].text.strip().replace(' ','')
            price=soup.select('div .trl-item')[0].text.strip()
            block=soup.select('.rcont #agantzfxq_C02_08')[0].text.strip()
            building=soup.select('.rcont #agantzfxq_C02_07')[0].text.strip()
            try:
                address=soup.select('.trl-item2 .rcont')[2].text.strip()
            except:
                address=soup.select('.trl-item2 .rcont')[1].text.strip()
            detail1=soup.select('.clearfix')[4].text.strip().replace('\n\n\n',',').replace('\n','')
            detail2=soup.select('.clearfix')[5].text.strip().replace('\n\n\n',',').replace('\n','')
            detail=detail1+detail2
            name=soup.select('.zf_jjname')[0].text.strip()
            buserid=re.search('buserid: \'(\d+)\'',res.text).group(1)
            phone=getPhone(buserid)
            print(title,price,block,building,address,detail,name,phone)
            house = (title, price, block, building, address, detail, name, phone)
            info.append(house)
            try:
                house_data=House(
                    title=title,
                    price=price,
                    block=block,
                    building=building,
                    address=address,
                    detail=detail,
                    name=name,
                    phone=phone
                )
                sess.add(house_data)
                sess.commit()
            except Exception as e:
                print(e)    # 打印错误信息
                sess.rollback()  # 回滚
        except:
            pass
    else:
        print(re.status_code,re.text)

# 获取代理人号码
def getPhone(buserid):
    url='https://zz.zu.fang.com/RentDetails/Ajax/GetAgentVirtualMobile.aspx'
    data['agentbid']=buserid
    res=session.post(url,data=data)
    if res.status_code==200:
        return res.text
    else:
        print(res.status_code)
        return

# 获取详细链接的线程池
async def Pool1(num):
    loop=asyncio.get_event_loop()
    task=[]
    with ThreadPoolExecutor(max_workers=5) as t:
        for i in range(0,3):
            url = f'https://zz.zu.fang.com/house/i3{i+1}/'
            task.append(loop.run_in_executor(t,getLink,url))

# 解析页面的线程池
async def Pool2(hrefs):
    loop=asyncio.get_event_loop()
    task=[]
    with ThreadPoolExecutor(max_workers=30) as t:
        for href in hrefs:
            task.append(loop.run_in_executor(t,parsePage,href))

if __name__ == '__main__':
    start_time=time.time()
    hrefs=[]
    info=[]
    task=[]
    init_url = 'https://zz.zu.fang.com/house/'
    num=getNum(getHtml(init_url))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(Pool1(num))
    print("共获取%d个链接"%len(hrefs))
    print(hrefs)
    loop.run_until_complete(Pool2(hrefs))
    loop.close()
    print("共获取%d条数据"%len(info))
    print("耗时{}".format(time.time()-start_time))
    session.close()
