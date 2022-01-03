import requests
import re
lis = []
# https://s.taobao.com/search?q=荣耀v20&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306
# https://s.taobao.com/search?q=荣耀v20&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=44
# https://s.taobao.com/search?q=荣耀V20&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=88
kv = {
    "user-agent":
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    "Cookie":
        'thw=cn; t=1414ebc1068c259f01fec665e2117552; enc=e962WciGaSzUdxZEtzwojV7uAXWPnRym%2B45XIy1MaPLZOoL037hBKPVCAfZMOueNq%2FXpBU5M1S3dtlDT891qwg%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; _samesite_flag_=true; cookie2=11ce951c08c7c65cd218767487509640; _tb_token_=3b71d63668373; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; mt=ci=0_0; cna=JcNvFpHpNlgCAd9aGTkCPnTd; v=0; _uab_collina=158011863290446529350021; JSESSIONID=E43D37DED38E5D1BDEE286F2D4E77CAB; unb=2942127069; uc1=cookie14=UoTUOqGfe%2B1Llg%3D%3D&cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&cookie15=VFC%2FuZ9ayeYq2g%3D%3D&cookie21=UtASsssme%2BBq&lng=zh_CN&pas=0&tag=8&existShop=false; uc3=nk2=roeNi8BqqvU%3D&lg2=URm48syIIVrSKA%3D%3D&id2=UUGmvJXOkb0M%2BQ%3D%3D&vt3=F8dBxdrLntgw4xZ5wZk%3D; csg=a99f98b4; lgc=%5Cu5916%5Cu53F7%5Cu73ED%5Cu957F; cookie17=UUGmvJXOkb0M%2BQ%3D%3D; dnk=%5Cu5916%5Cu53F7%5Cu73ED%5Cu957F; skt=63815ed9904eff32; existShop=MTU4MDEyNDE3OA%3D%3D; uc4=nk4=0%40rN3fFeAGJg4nh%2BSgCmANvVoT%2Fw%3D%3D&id4=0%40U2OR9MO3IpdxDQzZ0wct25B0gLdO; tracknick=%5Cu5916%5Cu53F7%5Cu73ED%5Cu957F; _cc_=Vq8l%2BKCLiw%3D%3D; tg=0; _l_g_=Ug%3D%3D; sg=%E9%95%BF9f; _nk_=%5Cu5916%5Cu53F7%5Cu73ED%5Cu957F; cookie1=U%2BM%2Ffnb25oWib9B234oPmGDMHwvfKN%2F6E7t4o8pzaxk%3D; isg=BNnZ9HXD42bvArw0v8-1A9iY6MWzZs0Y-VmB9PuOVYB_AvmUQ7bd6EcQBMZ0oWVQ; l=cBjHK7Krq8T5uNQEBOCanurza77OSIRYYuPzaNbMi_5CR6T1szbOoD-PNF96VjWdTMYB4q0AiPv9-etkZbBqmVlgGUMG.'
}

# 获取html页面
def getHTMLpages(url):
    try:
        r = requests.get(url, headers=kv, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


# 将商品信息存入列表
def getGoodsinfo(lis, html):
    # "raw_title":"honor/荣耀 荣耀play 微商手机 营销手机 小V  不凡 霸屏推"
    # "view_price":"6280.00"
    # "view_sales":"7人付款"或者"2.0万+人付款"或者"6000+人付款"
    title = re.findall(r'\"raw_title\"\:\".*?\"', html)  # .字符，*0或n次扩展，?表示最小匹配
    price = re.findall(r'\"view_price\"\:\"[\d.]*\"',
                       html)  # [\d.]*表示0-9或者.的0次或者多次取值
    sales = re.findall(r'\"view_sales\"\:\"[\d\.]*[\u4e00-\u9fa5]?\+?人付款\"',
                       html)  # [\u4e00-\u9fa5]表示中文字符
    for i in range(len(title)):
        tit = eval(title[i].split(':')[1])
        pri = eval(price[i].split(':')[1])
        sal = eval(sales[i].split(':')[1])
        lis.append([tit, pri, sal])
    # return lis


# 从列表中读取商品信息
def printGoodsinfo(lis):
    form = "{:^2}\t{:<50}\t{:>8}\t{:>8},"
    print(form.format("序号", "商品名称", "商品价格", "商品销量", chr(12288)))
    # for i in range(len(lis)):
    #     print("{:^3}\t{:^20}\t{:^10}\t{:^20}".format(i+1,lis[i][0],lis[i][1],lis[i][2],lis[i][3]))
    count = 1
    print()
    for i in lis:  # i代表一行
        print(form.format(count, i[0], i[1], i[2], chr(12288)))
        count += 1


if __name__ == "__main__":
    # f = open("D:\VscodePy\pytest\html.txt", encoding='utf-8')
    # sss = f.read()
    # f.close()
    s = input("请输入要查询的商品名称：")
    start_url = "https://s.taobao.com/search?q=" + s
    print(start_url)
    count = eval(input("请输入要查询的页数："))
    for i in range(count):
        url = start_url + '&s=' + str(i * 44)
        html = getHTMLpages(url)
        # print(html)
        getGoodsinfo(lis, html)
    # getGoodsinfo(lis, sss)
    printGoodsinfo(lis)
