# 破解sign值
import requests
import re
import execjs 
import json

headers = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    'Cookie':
        'PSTM=1575539987; BAIDUID=A80872D93185A688C8AC8CF159A4EF54:FG=1; BIDUPSID=3D8B9E5934B26CCEF003426B6773A431; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1455_21114_26350_30717; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; APPGUIDE_8_2_2=1; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1580901474,1580904731,1580905304,1580906217; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1580906217; yjs_js_security_passport=0fdd751f0722a3d0fb6a389e7fe2c2f2c9864c58_1580906237_js; __yjsv5_shitong=1.0_7_4a4fb445c2fea6132d704ca5e45285f82f61_300_1580906238325_223.91.220.158_37acdb4d; delPer=0; PSINO=1'
}

form_data = {
    # 'from': 'zh',
    # 'to': 'en',
    # 'query': word,
    'transtype': 'realtime',
    'simple_means_flag': '3',
    # 'sign': None,
    'token': '42e08df4cfc832413f5c96516ed21cc3'
}

# 获取sign的值
def getSign(word):
    with open('pytest\翻译接口\\fun_e(r).js', 'r', encoding='utf-8') as f:
        sign_js = execjs.compile(f.read())
        return sign_js.call('e', word)

# 获取结果的json数据
def getResult(url):
    try:
        r = requests.post(url, data=form_data, headers=headers, timeout=30)
        r.raise_for_status
        return r.text
    except:
        return ''
# 主函数
print("本程序同时支持汉译英和英译汉")
print("汉译英请输入1，英译汉请输入其他非0数字")
print("若想终止程序，请输入0")
while(True):
    a = eval(input("请输入数字："))
    if a == 1:
        f = 'zh'
        t = 'en'
    elif a==0:
        break
    else:
        f = 'en'
        t = 'zh'
    url_post = "https://fanyi.baidu.com/v2transapi"
    word = input("请输入要查询的字符：")
    sign = getSign(word)
    form_data['from'] = f
    form_data['to'] = t
    form_data['query'] = word
    form_data['sign'] = sign
    text = getResult(url_post)
    json_data = json.loads(text)
    # print(json_data)
    trans_result = json_data['trans_result']['data'][0]['dst']
    # print(trans_result)
    print("{}的翻译是：{}".format(word, trans_result))
print("程序退出运行！")
