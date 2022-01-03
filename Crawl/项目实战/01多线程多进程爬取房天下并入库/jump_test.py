import requests
import re

headers = {
    'referer': 'https://zz.zu.fang.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'cookie': 'global_cookie=ffzvt3kztwck05jm6twso2wjw18kl67hqft; city=zz; integratecover=1; __utma=147393320.427795962.1613371106.1613371106.1613371106.1; __utmc=147393320; __utmz=147393320.1613371106.1.1.utmcsr=zz.fang.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt_t0=1; __utmt_t1=1; __utmt_t2=1; ASP.NET_SessionId=aamzdnhzct4i5mx3ak4cyoyp; Rent_StatLog=23d82b94-13d6-4601-9019-ce0225c092f6; Captcha=61584F355169576F3355317957376E4F6F7552365351342B7574693561766E63785A70522F56557370586E3376585853346651565256574F37694B7074576B2B34536C5747715856516A4D3D; g_sourcepage=zf_fy%5Elb_pc; unique_cookie=U_ffzvt3kztwck05jm6twso2wjw18kl67hqft*6; __utmb=147393320.12.10.1613371106',
    'referer': 'https://zz.zu.fang.com/chuzu/3_181846453_1.htm?rfss=1-41919ea4acac9a8d9e-28'
}
data={
    # 'houseId':181846453,
    # 'sourceUrl': 'https%3A//zz.zu.fang.com/chuzu/3_181846453_1.htm%3Frfss%3D1-41919ea4acac9a8d9e-28',
    # 'guid': 'ffzvt3kztwck05jm6twso2wjw18kl67hqft',
    'agentbid': '1034514'
}

# url='https://zz.zu.fang.com/RentDetails/Ajax/GetAgentVirtualMobile.aspx'
url='https://zz.zu.fang.com/chuzu/3_181846453_1.htm?rfss=1-41919ea4acac9a8d9e-28'
res=requests.get(url,headers=headers)
print(res.status_code)
print(res.text)
buserid=re.search('buserid: \'(\d+)\'',res.text).group(1)
print(buserid)
# print(re.text)
