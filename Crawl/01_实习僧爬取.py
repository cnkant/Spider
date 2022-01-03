import requests
from bs4 import BeautifulSoup
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

def getPage(url):
    re=requests.get(url,headers=headers)
    return re.text

# 获取详细信息
def getDetail(html):
    soup=BeautifulSoup(html,'lxml')
    # title=soup.title.text #获取网页标题
    job_name=soup.select('.new_job_name span')[0].text.strip()
    company_name=soup.select('.com_intro .com-name')[0].text.strip()
    salary=getNumber(soup.select('.job_money')[0].text.strip())
    job_week=getNumber(soup.select('.job_week')[0].text.strip())
    job_time=getNumber(soup.select('.job_time')[0].text.strip())
    # print("{:<20}{:<20}{:<10}{:<10}{:<10}".format(job_name,company_name,salary,job_week,job_time))
    print(job_name,company_name,salary,job_week,job_time)

# 字符串解密
def getNumber(text):
    text=text.encode('utf-8')
    text = text.replace(b'\xee\xac\xb1', b'0')
    text = text.replace(b'\xee\x99\xbc', b'1')
    text = text.replace(b'\xef\x82\x81', b'2')
    text = text.replace(b'\xee\xb2\x99', b'3')
    text = text.replace(b'\xef\x97\x92', b'4')
    text = text.replace(b'\xef\x8e\x93', b'5')
    text = text.replace(b'\xef\x96\x9f', b'6')
    text = text.replace(b'\xee\xb8\xb4', b'7')
    text = text.replace(b'\xef\x9e\xb1', b'8')
    text = text.replace(b'\xef\xa1\x99', b'9')
    # 将utf-8的编码解码为字符串,不加这一句，文字和数字均是utf-8编码
    text = text.decode()
    return text

if __name__ == '__main__':
    # print("{:<20}{:<20}{:<10}{:<10}{:<10}".format("职位名称", "公司名称", "薪资", "实习天数", "实习月数"))
    url="https://www.shixiseng.com/interns?page=1&type=intern&keyword=Python&city=北京"
    html_1=getPage(url)
    soup=BeautifulSoup(html_1,'lxml')
    count=soup.select('.el-pager .number')[-1].text # 页数
    for i in range(1,int(count)+1):
        print(">>>开始爬取第{}页".format(i))
        url='https://www.shixiseng.com/interns?page={}&type=intern&keyword=Python&city=北京'.format(i)
        html=getPage(url) # 获取每个page的url
        soup=BeautifulSoup(html,'lxml')
        for item in soup.select('.f-l .intern-detail__job a'):
            url_detail=item['href'] #每个职位的详细链接
            html=getPage(url_detail)
            getDetail(html)
