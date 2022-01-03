import requests
import time
from bs4 import BeautifulSoup

headers={
    'cookie': '_octo=GH1.1.341208026.1588205682; _ga=GA1.2.66233726.1588205694; _device_id=07ee65b4c6b2580a460be3bea908442a; has_recent_activity=1; tz=Asia%2FShanghai; logged_in=no; _gh_sess=N6UqppSN%2B95qm7wu5fWnxUdehWqvHuEu9q2itpbWlQw4uCCdG4XPQD%2B1jFLuoBLgcKG94nmLbs9YM8DmzBSp04bw0PjiPIiiQ4%2FL9W3T%2BoiGmTzJvwi7VQJcVOt9hjrPSpEb9vd46Z58q0WxNckpukfppmCnkHsLKUnpxsI0zdIA7QjViMoeLx3woESHc5v6GzQ7yXXx2Uo35x%2BtbIpjBlsHZ5O1QOWG7SDcvB5CUeRR3N7ObAkd96j8YW%2FC3nmDi9tUv7BTbrGoHVZM2EYMMsF9cZxRBLZuazsiVYDF6s7hTXh1k4yk0Cqs%2BEsX7HpJQfZkDEq7%2FyG6gZ7SL8KXSJFnS3IAyFvKQw58Ge5cDjeg%2BCdWhCo8Iz%2BXsf4QrUw%2BWmzuBx5LcXj7CF9jsQe8Qj6Ciyv2q3cDhGFKhJ%2FW1RiJyOlO7%2FeSjr7qtHWLfMyJNDDkSNCoNrW8rruDDyX%2BInbizr7O7Jiy0EtTfrIREN7G716%2BCjQcD0S3WscAQ6fCyvDW2W9ChpvY7gOSYnb6xhzADXSgLJQQ6pJ%2BzcLsePkcREvt7xsHVKV1MN3JRBnFGR%2BbnT0wyh7Y9%2B44pwHlMo3FMV83n31PW1HdlDi7pGhSxDWnGNs9lm5rwRTEXtG95BXrc9%2FJARNw28Flm09CZn5cqqblPJkjgsXJJfzRrM1GT%2FfAqOyQVQRWbuKe1RfNSzKVW3l0BYx58Jl1F9EvODN28y0hyNsZXfUslY4AJmGV2yJTVvV7zS6aS%2BiTR5vnKKfr7V9cF0WbxDfaIHdGPA2zaewCOOSCcw%2BiUBvHx8CUNWz41X5LcEBPC1rv9aogLLmDqh7KAYs%2FOeal67CUNqmmGnFGrOGrgTOc%2BWHNzbVBH5ih5Ih6qkKAM%2BuwcVWg9yAjRsk4ncip2F73JBZ3ItPv9eTnjm7A0s1mBSNSrBfmeQ9csYuzhEnZbEiuxsBhWlVMqAEkcTrmZ3F1vbVCet5OJ2N4NWEQC2tItuzjebY7r86UbTEGPBszw2Y%3D--MLNOOpXl7Jznpg4o--vY5cgdsaYbt40japybXUMA%3D%3D',
    'referer': 'https://github.com/session',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
data={
    'commit': 'Sign in',
    'authenticity_token': 'vBwUVlgPyw/nAtTvE9vUbKeT8QVn2SQaaZRu4XZ9AWE7x+dgEXmmDCvGLIjaASh5+Z+6EyADzS6Vnna0NMJ0hQ==',
    'login': '',
    'password': '',
    'webauthn-support': 'supported',
    'webauthn-iuvpaa-support': 'unsupported',
    'timestamp': '{}'.format(time.time()),
    'timestamp_secret': 'b1a08bd09e48a13f10143221a1a725f0c878ddb2444f253e4dfa006b4cfd3da9'
}

session=requests.session()
session.headers=headers

# 获取登陆页面
def getPage(url):
    re=session.post(url,data=data,headers=headers)
    if re.status_code==200:
        # with open('07_github.html','w',encoding='utf8') as f:
        #     f.write(re.text)
        print("登录成功")
        print("开始获取动态...")
        getNews(session)
        print("获取完毕")
    else:
        print(re.status_code)

# 获取关注动态
def getNews(sess):
    url_2='https://github.com/dashboard-feed'
    res=sess.get(url_2)
    try:
        res.encoding=res.apparent_encoding
        soup=BeautifulSoup(res.text,'lxml')
        contents=soup.select('.watch_started')
        for item in contents:
            author=item.select('.d-flex .flex-items-baseline a')[0].text
            project=item.select('.d-flex .flex-items-baseline a')[1].text
            print("author:{}\tstarred:{}".format(author,project))

    except:
        print("获取动态失败！")

if __name__ == '__main__':
    url='https://github.com/session'
    login=input("用户名：")
    password=input("密码：")
    data['login']=login
    data['password']=password
    getPage(url)
