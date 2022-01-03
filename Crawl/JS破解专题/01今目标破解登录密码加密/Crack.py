import requests
import execjs

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
data={
    'login_type': 'default',
    'username': '',
    'password': ''
}
def getPage(url):
    re=requests.post(url,data=data,headers=headers)
    print(re.status_code)
    re.encoding=re.apparent_encoding
    return re.text

def decode_pw(password):
    with open('sha1加密.js','r',encoding='utf-8') as f:
        content=f.read()
    jsdata=execjs.compile(content)
    pwd=jsdata.call('Sha1',password)
    print(pwd)
    return pwd

if __name__ == '__main__':
    url='https://sso.jingoal.com/oauth/authorize'
    username=input("用户名：")
    password=input("密码：")
    data['username']=username
    data['password']=decode_pw(password)
    html=getPage(url)
