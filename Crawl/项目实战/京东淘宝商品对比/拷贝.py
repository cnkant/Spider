import requests
import re
import openpyxl  # 操作xlsx格式的Excel
import json
import csv
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib as mpl
from bs4 import BeautifulSoup
import numpy as np
list = []
kv = {
    "user-agent":
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    "Cookie":
        'thw=cn; t=1414ebc1068c259f01fec665e2117552; enc=e962WciGaSzUdxZEtzwojV7uAXWPnRym%2B45XIy1MaPLZOoL037hBKPVCAfZMOueNq%2FXpBU5M1S3dtlDT891qwg%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; _samesite_flag_=true; cookie2=11ce951c08c7c65cd218767487509640; _tb_token_=3b71d63668373; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; mt=ci=0_0; cna=JcNvFpHpNlgCAd9aGTkCPnTd; v=0; _uab_collina=158011863290446529350021; JSESSIONID=E43D37DED38E5D1BDEE286F2D4E77CAB; unb=2942127069; uc1=cookie14=UoTUOqGfe%2B1Llg%3D%3D&cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&cookie15=VFC%2FuZ9ayeYq2g%3D%3D&cookie21=UtASsssme%2BBq&lng=zh_CN&pas=0&tag=8&existShop=false; uc3=nk2=roeNi8BqqvU%3D&lg2=URm48syIIVrSKA%3D%3D&id2=UUGmvJXOkb0M%2BQ%3D%3D&vt3=F8dBxdrLntgw4xZ5wZk%3D; csg=a99f98b4; lgc=%5Cu5916%5Cu53F7%5Cu73ED%5Cu957F; cookie17=UUGmvJXOkb0M%2BQ%3D%3D; dnk=%5Cu5916%5Cu53F7%5Cu73ED%5Cu957F; skt=63815ed9904eff32; existShop=MTU4MDEyNDE3OA%3D%3D; uc4=nk4=0%40rN3fFeAGJg4nh%2BSgCmANvVoT%2Fw%3D%3D&id4=0%40U2OR9MO3IpdxDQzZ0wct25B0gLdO; tracknick=%5Cu5916%5Cu53F7%5Cu73ED%5Cu957F; _cc_=Vq8l%2BKCLiw%3D%3D; tg=0; _l_g_=Ug%3D%3D; sg=%E9%95%BF9f; _nk_=%5Cu5916%5Cu53F7%5Cu73ED%5Cu957F; cookie1=U%2BM%2Ffnb25oWib9B234oPmGDMHwvfKN%2F6E7t4o8pzaxk%3D; isg=BNnZ9HXD42bvArw0v8-1A9iY6MWzZs0Y-VmB9PuOVYB_AvmUQ7bd6EcQBMZ0oWVQ; l=cBjHK7Krq8T5uNQEBOCanurza77OSIRYYuPzaNbMi_5CR6T1szbOoD-PNF96VjWdTMYB4q0AiPv9-etkZbBqmVlgGUMG.'
}
jd={
    "user-agent":
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
    "Cookie":
        '__jdv=76161171|baidu|-|organic|%25E4%25BA%25AC%25E4%25B8%259C|1590021947460; __jdu=1590021947458207094210; areaId=7; ipLoc-djd=7-458-466-0; shshshfpa=bb2aeedc-e109-4ece-1306-775cd7d03883-1590021950; shshshfpb=goqrbqPRqnCnHrGn%2FNAOmtg%3D%3D; user-key=25b5e21c-56ae-4894-bfc2-7d45bbc5da13; cn=0; jwotest_product=99; __jda=122270672.1590021947458207094210.1590021947.1590026171.1590032625.3; __jdc=122270672; shshshfp=4ec0c05907fbcd17f8173943888ec271; 3AB9D23F7A4B3C9B=JS4WWIGBKCACP5JPLRHYGTYLTJ2S7AYH6JLTJ4Z7SUG3NY7OITSW7NXP7SXYQYULI5Y6NXFROS5KWQ2YTUZ75ETJMM; JSESSIONID=95CD4C236695D8152995C6EBCCA4BDBF.s1; shshshsID=ebc07e1a58fc7ea089a7e3799f23f11e_7_1590034787783; __jdb=122270672.7.1590021947458207094210|3.1590032625',
    "Host":
        "club.jd.com"
    # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    # "Accept-Encoding": "gzip, deflate, br",
    # "Accept-Language": "zh-CN,zh;q=0.9",
    # "Cache-Control": "max-age=0",
    # "Connection": "keep-alive",
    # "Sec-Fetch-Dest": "document",
    # "Sec-Fetch-Mode":"navigate",
    # "Upgrade-Insecure-Requests": "1",
    # "Sec-Fetch-Site": "none",
    # "Sec-Fetch-User": "?1"
}
form_data={
    "callback": "fetchJSON_comment98",
    "productId": "100011336064",
    "score": "0",
    "sortType": "5",
    "page": "0",
    "pageSize": "10",
    "isShadowSku": "0",
    "fold": "1"
}
# 获取淘宝HTML页面
def getHTMLpages(url):
    try:
        r = requests.get(url, headers=kv, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

# 获取京东HTML页面
def getHTMLpages_JD(url):
    try:
        r=requests.get(url,headers=jd)
        # print(r.status_code)
        # r.raise_for_status()
        page_connent = r.content.decode('gbk')
        # print(page_connent)
        return page_connent
    except:
        return "异常"

# 将淘宝商品信息存入列表
def getGoodsinfo(list, html, flag):
    if flag == 0:
        tit = "荣耀v30手机"
    elif flag == 1:
        tit = "小米10手机"
    else:
        tit = "vivoS6手机"
    # title = re.findall(r'\"raw_title\"\:\".*?\"', html)  # .字符，*0或n次扩展，?表示最小匹配
    # price = re.findall(r'\"view_price\"\:\"[\d.]*\"',html)  # [\d.]*表示0-9或者.的0次或者多次取值
    sales = re.findall(r'\"comment_count\"\:\"[\d]*?\"',
                       html)  # [\u4e00-\u9fa5]表示中文字符
    # for i in range(len(title)):
    # tit = eval(title[0].split(':')[1])
    # pri = eval(price[0].split(':')[1])
    sal = eval(sales[0].split(':')[1])
    # print(tit)
    # print(pri)
    # print(sal)
    list.append([tit, "淘宝", sal])
    return list

# 将京东商品信息存入列表
def getGoodsinfo_JD(list,html_jd,flag):
    if flag == 0:
        tit = "荣耀v30手机"
    elif flag == 1:
        tit = "小米10手机"
    else:
        tit = "vivoS6手机"
    sales=re.findall(r'\"commentCount\"\:[\d]*',html_jd)
    # print(sales)
    sal = eval(sales[0].split(':')[1])
    # print(tit)
    # print(sal)
    list.append([tit,"京东",sal])

# 从列表中读取商品信息
def printGoodsinfo(list):
    form = "{:<10}\t\t{:<10}\t{:<8}"
    print(form.format("手机型号", "销售平台", "商品销量", chr(12288)))
    print()
    for i in list:  # i代表一行
        print(form.format(i[0], i[1],i[2], chr(12288)))

# 保存数据为csv文件
def saveData(list):
    try:
        f=open('pytest\京东淘宝商品对比\GoodsInfo.csv','w',newline='',encoding='gbk') # 1. 创建文件对象
        # newline=''是为了去掉每条数据下面的空行
        csv_writer = csv.writer(f) # 2. 基于文件对象构建 csv写入对象
        csv_writer.writerow(["手机型号","销售平台","商品销量"]) # 3. 构建列表头
        # 4. 写入csv文件内容
        for i in range(len(list)):
            csv_writer.writerow(list[i])
        f.close()
        print("保存成功！文件为同一目录下的GoodsInfo.csv")
    except:
        print("保存失败！")

# 根据csv文件绘图
def drawData(list):
    fig,ax=plt.subplots()
    mpl.rcParams["font.sans-serif"] = ["SimHei"]
    mpl.rcParams["axes.unicode_minus"] = False
    x = np.arange(3)
    count_taobao=[]
    count_jd=[]
    for i in range(len(list)):
        if(i%2==0): # 下标0、2、4为淘宝销量
            count_taobao.append(int(list[i][2]))
        else: # 下标1、3、5为京东销量
            count_jd.append(list[i][2])
    print(count_taobao)
    print(count_jd)
    bar_width = 0.35
    tick_label = ["荣耀V30手机", "小米10手机", "vivoS6手机"]
    plt.bar(x, count_taobao, bar_width, align="center", color="c", label="淘宝平台", alpha=0.5)
    plt.bar(x+bar_width, count_jd, bar_width, color="b", align="center", label="京东平台", alpha=0.5)
    plt.xlabel("手机型号")
    plt.ylabel("平台销量")
    ax.set_title("三种型号手机在京东和淘宝销量对比图") #设置标题
    plt.xticks(x+bar_width/2, tick_label)
    plt.legend()
    plt.savefig('pytest\京东淘宝商品对比\\drawData.png')
    plt.show()

if __name__ == "__main__":
    # f = open("D:\VscodePy\pytest\html.txt", encoding='utf-8')
    # sss = f.read()
    # f.close()
    print("该程序将自动分别爬取华为荣耀V30、小米10和vivoS6手机在淘宝和京东的销量")
    print("程序即将开始执行......")

    print("开始爬取华为荣耀V30在淘宝的销量数据...")
    start_url_taobao = "https://s.taobao.com/search?q=" + "荣耀v30" + "&sort=sale-desc"
    html = getHTMLpages(start_url_taobao)
    getGoodsinfo(list, html, 0)

    print("开始爬取华为荣耀V30在京东的销量数据...")
    start_url_jd="https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100010260230&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1"
    html_jd=getHTMLpages_JD(start_url_jd)
    # print(html_jd)
    getGoodsinfo_JD(list,html_jd,0)

    print("开始爬取小米10在淘宝的销量数据...")
    start_url_taobao = "https://s.taobao.com/search?q=" + "小米10手机" + "&sort=sale-desc"
    html = getHTMLpages(start_url_taobao)
    getGoodsinfo(list, html, 1)

    print("开始爬取小米10在京东的销量数据...")
    start_url_jd="https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100011336064&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1"
    html_jd=getHTMLpages_JD(start_url_jd)
    getGoodsinfo_JD(list ,html_jd,1)

    print("开始爬取vivoS6在淘宝的销量数据...")
    start_url_taobao = "https://s.taobao.com/search?q=" + "vivoS6" + "&sort=sale-desc"
    html = getHTMLpages(start_url_taobao)
    getGoodsinfo(list, html, 2)

    print("开始爬取vivoS6在京东的销量数据...")
    start_url_jd="https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100011924580&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1"
    html_jd=getHTMLpages_JD(start_url_jd)
    getGoodsinfo_JD(list,html_jd,2)
    # getGoodsinfo(list, sss)
    print("爬取完毕！结果如下：")
    printGoodsinfo(list)
    print("现在将数据存入CSV文件中...")
    saveData(list)
    print("现在将数据可视化展示出来：")
    drawData(list)
