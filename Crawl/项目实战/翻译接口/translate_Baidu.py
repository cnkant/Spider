import requests
import json

word = input("请输入你要查询的单词(汉译英/英译汉)：")
kv = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}
form_data = {'kw': word}
post_url = "https://fanyi.baidu.com/sug"
response = requests.post(post_url, data=form_data, headers=kv, timeout=30)
# print(response.content.decode())
result = json.loads(response.content.decode())
# print(result)
print("“{}”的意思如下".format(word))
for i in range(len(result["data"])):
    print(result["data"][i]["k"])
    print(result["data"][i]["v"])
