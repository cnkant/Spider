# 此代码没有破解sign值
import requests
import json

word = input("请输入你要查询的单词(汉译英)：")
kv = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    # "Host":
    #     "fanyi.baidu.com",
    # "Origin":
    #     "https://fanyi.baidu.com",
    # "X-Requested-With":
    #     "XMLHttpRequest",
    # "Referer":
    #     "https://fanyi.baidu.com/?aldtype=16047",
    'Cookie':
        'PSTM=1575539987; BAIDUID=A80872D93185A688C8AC8CF159A4EF54:FG=1; BIDUPSID=3D8B9E5934B26CCEF003426B6773A431; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1455_21114_26350_30717; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; APPGUIDE_8_2_2=1; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1580901474,1580904731,1580905304,1580906217; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1580906217; yjs_js_security_passport=0fdd751f0722a3d0fb6a389e7fe2c2f2c9864c58_1580906237_js; __yjsv5_shitong=1.0_7_4a4fb445c2fea6132d704ca5e45285f82f61_300_1580906238325_223.91.220.158_37acdb4d; delPer=0; PSINO=1'
}

form_data = {
    'from': 'zh',
    'to': 'en',
    'query': word,
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '944849.690656',
    'token': '42e08df4cfc832413f5c96516ed21cc3'
}


def getPages(url):
    try:
        response = requests.post(url, data=form_data, headers=kv)
        response.raise_for_status()
        return response.content.decode()
    except:
        return "异常"


post_url = "https://fanyi.baidu.com/v2transapi?from=zh&to=en"
response = getPages(post_url)
# print(response)
result = json.loads(response)
# print(result)
print("“{}”的翻译成英文是：".format(word))
print(result["trans_result"]["data"][0]["dst"])
